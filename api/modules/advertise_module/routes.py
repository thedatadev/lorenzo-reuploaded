from flask import jsonify, request
from flask import current_app as app # Note: only available inside context of a request
import datetime
import jwt
import pprint
import time

from modules.database_module.models import Listing, User, Booking
from modules.database_module.shared_db import db
from modules.advertise_module import mod
from modules.shared_methods import deserialize, login_required, get_user, sanitize_dict_keys
from modules.google_api import Googlemap_api

from modules.advertise_module.helper import (sanitize_listings, get_coordinates, 
                                             preprocess_amenities, generate_img_uri)

gmap_api = Googlemap_api()

# Route to create new listing
@mod.route('/listing', methods=['POST'])
@login_required
def new_listing():
    ''' Create a new listing in the database (with main fields only) '''    
    try:
        # Extract the form data
        form_data = request.form
        # Derive the long/lat from address
        longitude, latitude = get_coordinates(form_data['address'])
        # Ensure amenities is in same format as dataset i.e. {"Wifi", "TV", ... "Pool"}
        amenities_cleansed = preprocess_amenities(form_data['amenities'])
        # Save the image to S3 and generate an image URI to store in RDS
        img_uri = generate_img_uri(request)
        # Add new listing to db
        new_listing = Listing(
            name = form_data['name'], 
            description = form_data['description'], 
            neighbourhood = form_data['neighbourhood'], 
            property_type = form_data['property_type'], 
            room_type = form_data['room_type'],
            accommodates = int(form_data['accommodates']), 
            price = float(form_data['price']), 
            transit = form_data['transit'], 
            address = form_data['address'], 
            bedrooms = int(form_data['bedrooms']), 
            beds = int(form_data['beds']), 
            bathrooms = int(form_data['bathrooms']),
            amenities = amenities_cleansed, 
            minimum_nights = int(form_data['minimum_nights']), 
            maximum_nights = int(form_data['maximum_nights']), 
            longitude = longitude, 
            latitude = latitude,
            house_rules = form_data['house_rules'], 
            picture_url = img_uri, 
            host_id = get_user(request)
        )
        # Commit changes
        db.session.add(new_listing)
        db.session.commit()
        print("Listing ID for new listing:", new_listing.id)
        return '', 200

    except Exception as e:
        print(e)
        return '', 404

# Route to fetch listings posted by a user
@mod.route('/listings/advertise', methods=['GET'])
@login_required
def get_advertised_listings():
    ''' Retrieve a user's advertised listings '''
    user = get_user(request)
    listings = db.session.query(Listing).filter_by(host_id = user).all()
    listings = sanitize_listings(listings)
    return jsonify(listings=listings), 200
