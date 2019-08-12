from flask import current_app as app
from flask import jsonify, request

import calendar
import math
import operator
import pickle
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
from google.protobuf.json_format import MessageToJson
import json

from modules.database_module.models import Booking, Conversation, Listing, User
from modules.database_module.shared_db import db
from modules.search_module import mod
from modules.search_module.recommend import recommend
from modules.search_module.search_engine import SearchEngine
from modules.shared_methods import deserialize, login_required
from modules.search_module.helper import (sanitize_listings, get_places_of_interest, 
                                          dot_product2, vector_cos5, get_recommendations_vecs,
                                          get_calendar_availabilites)

search_engine = SearchEngine()

TOP_K_RESULTS = 10

df = pd.read_csv(r'modules/search_module/db3.csv', index_col=0)

recommendations_vecs = get_recommendations_vecs()


## Listing search

@mod.route("/search/<int:conversation_id>", methods=['GET'])
@login_required
def get_search_results(conversation_id):
    ''' Retrieving search results for a conversation '''
    # Identify conversation
    topk = 10
    conversation = db.session.query(Conversation).filter_by(
        id=conversation_id).first()
    # Extract query params
    query_params = deserialize(conversation.query_params)
    # Run search
    search_results, id_list = search_engine.search(query_params, df)
    query_params = json.loads(MessageToJson(query_params))
    if not search_results:
        #TODO add a prompt to user we cant find anything
        search_results = recommend(df, query_params)
    elif len(search_results) < topk:
        search_results2 = recommend(df, query_params, True,
                                    topk - len(search_results), id_list)
        search_results += search_results2
    elif len(search_results) == topk:
        pass
    # Return search results
    return jsonify(listings=search_results), 200

@mod.route("/listings/<int:listing_id>", methods=['GET'])
@login_required
def get_listing(listing_id):
    ''' Retrieve individual listing '''
    listing = Listing.get_listing(listing_id)
    ret = listing.__dict__
    ret = {k: v for k, v in ret.items() if not k.startswith("_")}
    ret['places'] = get_places_of_interest(listing)
    return jsonify(listing=ret), 200

@mod.route("/available_dates/<int:listing_id>")
@login_required
def get_available_dates(listing_id):
    ''' Retrieve booking availabilities for a given listing '''
    bookings = Booking.get_bookings_by_listing(listing_id)
    booked = []
    for booking in bookings:
        # TODO filter by month
        for i in range(booking.num_nights):
            d = booking.start_date + timedelta(i)
            booked.append(d.day)
    booked = set(booked)
    current_date = datetime.now()
    six_month_dates = []
    # Get availabilities for the next six months
    for m in range(6):
        next_month = current_date.month
        next_year = current_date.year
        six_month_dates.append(get_calendar_availabilites(booked, next_year, next_month))
        current_date += relativedelta(months=+1)
    # Calc the current month's month index (for frontend display purposes)
    month_index = datetime.now().month - 1
    return jsonify(calendar=six_month_dates, base_month=month_index), 200



## Listing recommendations

@mod.route("/listing_recommendations/<int:listing_id>", methods=['GET'])
@login_required
def get_similar_listings(listing_id):
    ''' Recommend listings most similar to a given listing '''
    listing = Listing.get_listing(listing_id)
    reccs = [(x[0], vector_cos5(listing.as_vector, x[1]))
             for x in recommendations_vecs.items()]
    sorted_vecs = sorted(
        reccs, key=lambda x: x[1], reverse=True)[:TOP_K_RESULTS]
    summarised = []
    for listing_id, _ in sorted_vecs:
        listing = db.session.query(Listing).filter_by(id=listing_id).first()
        summarised.append(listing)
    listings = sanitize_listings(summarised)
    return jsonify(listings=listings), 200