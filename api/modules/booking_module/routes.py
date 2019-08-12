from flask import jsonify, request
from flask import current_app as app # Note: only available inside context of a request
import dateutil.parser

from modules.booking_module import mod

from modules.database_module.models import Booking, Conversation, Listing, User
from modules.database_module.shared_db import db
from modules.shared_methods import (deserialize, get_user, login_required,
                                    sanitize_dict_keys)

def sanitize_bookings(bookings):
    ''' Filter out metadata keys in each booking, only keep column field names like "start_date" '''
    ret = []
    if bookings:
        ret = [sanitize_dict_keys(booking) for booking in bookings]
    return ret

@mod.route("/listings/<int:listing_id>/bookings", methods=['POST'])
@login_required
def create_booking_for_listing(listing_id):
    ''' Creates a booking for a user, given the listing '''
    try:
        ## Extract POST body
        post_json = request.json

        ## Parse date
        parsed_date = dateutil.parser.parse(post_json['start_date'])
        year = str(parsed_date.year)
        month = parsed_date.month
        month = '0' + str(month) if month < 10 else str(month)
        day = parsed_date.day
        day = '0' + str(day) if day < 10 else str(day)
        start_date = year + month + day

        ## Convert num nights
        num_nights = int(post_json['num_nights'])

        ## Get user
        user_id = get_user(request)

        booking = Booking(
            listing_id=listing_id,
            user_id=user_id,
            start_date=start_date,
            num_nights=num_nights)
        db.session.add(booking)
        db.session.commit()
    except Exception as e:
        print(e)
        return '', 401  # something went wrong

    return '', 200


@mod.route("/user/bookings", methods=['GET'])
@login_required
def get_user_bookings():
    ''' Retrieve all bookings made by a user '''
    ## Get user
    user_id = get_user(request)
    bookings = Booking.get_bookings_by_user(user_id)
    bookings = sanitize_bookings(bookings)
    ## Add info about the booking's listing
    for booking in bookings:
        listing = db.session.query(Listing).filter_by(
            id=booking['listing_id']).first()
        booking['listing_room_type'] = listing.room_type
        booking['listing_property_type'] = listing.property_type
        booking['price'] = listing.price
        booking['neighbourhood'] = listing.neighbourhood
        booking['picture_url'] = listing.picture_url

    return jsonify(bookings=bookings), 200

