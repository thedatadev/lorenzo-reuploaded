from modules.database_module.shared_db import db
from datetime import datetime
RECOMMENDER_LISTINGS_LIMIT = 5


## User model
class User(db.Model):
    ''' User table schema 

    Each User may have many conversations (1-to-Many)
    
    '''
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    query = db.relationship('Conversation', backref='user')


## Conversation model
class Conversation(db.Model):
    ''' Conversation table schema '''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    chat_history = db.Column(db.Text)
    query_params = db.Column(db.Text)


## Booking Model
class Booking(db.Model):
    ''' Booking table schema '''
    __bind_key__ = 'listings_db'
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(
        'listing_id',
        db.Integer,
        db.ForeignKey('listing.id'),
        nullable=False,
        index=True,
        unique=False)
    user_id = db.Column(db.Integer, nullable=False)
    start_date = db.Column(
        db.DateTime, default=datetime.utcnow)
    num_nights = db.Column(db.Integer)

    @classmethod
    def get_bookings_by_listing(cls, listing_id):
        bookings = db.session.query(cls).filter(
            Booking.listing_id == listing_id).all()
        return bookings

    @classmethod
    def get_bookings_by_user(cls, user_id):
        bookings = db.session.query(cls).filter(
            Booking.user_id == user_id).all()
        return bookings


## Listing model
class Listing(db.Model):
    ''' Listing table schema '''

    __bind_key__ = 'listings_db'  # required to bind this model to the listings database
    # (instead of main_db which is the default db)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    summary = db.Column(db.Text)
    description = db.Column(db.Text)
    neighbourhood = db.Column(db.Text)
    notes = db.Column(db.Text)
    transit = db.Column(db.Text)
    access = db.Column(db.Text)
    interaction = db.Column(db.Text)
    house_rules = db.Column(db.Text)
    picture_url = db.Column(db.Text)
    host_id = db.Column(db.Integer)
    host_name = db.Column(db.Text)
    host_since = db.Column(db.Text)
    host_location = db.Column(db.Text)
    host_about = db.Column(db.Text)
    host_response_time = db.Column(db.Text)
    host_response_rate = db.Column(db.Text)
    host_thumbnail_url = db.Column(db.Text)
    host_picture_url = db.Column(db.Text)
    host_neighbourhood = db.Column(db.Text)
    neighbourhood_cleansed = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zipcode = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    property_type = db.Column(db.Text)
    room_type = db.Column(db.Text)
    accommodates = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    bedrooms = db.Column(db.Integer)
    beds = db.Column(db.Integer)
    amenities = db.Column(db.Text)
    price = db.Column(db.Float)
    weekly_price = db.Column(db.Float)
    monthly_price = db.Column(db.Float)
    security_deposit = db.Column(db.Float)
    cleaning_fee = db.Column(db.Float)
    guests_included = db.Column(db.Integer)
    extra_people = db.Column(db.Text)
    minimum_nights = db.Column(db.Integer)
    maximum_nights = db.Column(db.Integer)
    availability_30 = db.Column(db.Integer)
    availability_60 = db.Column(db.Integer)
    availability_90 = db.Column(db.Integer)
    availability_365 = db.Column(db.Integer)
    review_scores_rating = db.Column(db.Integer)
    review_scores_accuracy = db.Column(db.Integer)
    review_scores_cleanliness = db.Column(db.Integer)
    review_scores_checkin = db.Column(db.Integer)
    review_scores_communication = db.Column(db.Integer)
    review_scores_location = db.Column(db.Integer)
    review_scores_value = db.Column(db.Integer)

    def __init__(self, name, description, neighbourhood, property_type, room_type,
                       accommodates, price, transit, address, bedrooms, bathrooms,
                       amenities, minimum_nights, maximum_nights, longitude, latitude,
                       house_rules, picture_url, beds, host_id):
        self.name = name
        self.description = description
        self.neighbourhood = neighbourhood
        self.property_type = property_type
        self.room_type = room_type
        self.accommodates = accommodates
        self.price = price
        self.transit = transit
        self.address = address
        self.bedrooms = bedrooms
        self.beds = beds
        self.bathrooms = bathrooms
        self.amenities = amenities
        self.minimum_nights = minimum_nights
        self.maximum_nights = maximum_nights
        self.longitude = longitude
        self.latitude = latitude
        self.house_rules = house_rules
        self.picture_url = picture_url
        self.host_id = host_id

    @classmethod
    def get_listing(cls, listing_id):
        listing = db.session.query(cls).filter(
            Listing.id == listing_id).first()
        return listing

    @property
    def as_vector(self):
        return [
            getattr(self, x) for x in [
                "accommodates", 'price', 'latitude', 'longitude',
                'review_scores_rating'
            ]
        ]

    @classmethod
    def get_similar_listings(cls, listing_id):
        # TODO make this more useful
        base_listing = cls.get_listing(listing_id)

        similar_listings = db.session.query(cls).filter(
            cls.accommodates == base_listing.accommodates).limit(
                RECOMMENDER_LISTINGS_LIMIT)
        if similar_listings:
            return similar_listings
        else:
            return None