import calendar
import math
import operator
import pickle
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

from modules.google_api import Googlemap_api
from modules.shared_methods import sanitize_dict_keys

gmap_api = Googlemap_api()


def sanitize_listings(listings):
    ''' Filter out metadata keys for each listing '''
    ret = []
    if listings:
        ret = [sanitize_dict_keys(listing) for listing in listings]
    return ret

def get_places_of_interest(listing):
    ''' Find places of interest in the vicinity of a given lng/lat coordinate '''
    location = {'lat': listing.latitude, 'lng': listing.longitude}
    places = gmap_api.return_nearby(location)
    return places


def dot_product2(v1, v2):
    return sum(map(operator.mul, v1, v2))


def vector_cos5(v1, v2):
    prod = dot_product2(v1, v2)
    len1 = math.sqrt(dot_product2(v1, v1))
    len2 = math.sqrt(dot_product2(v2, v2))
    return prod / (len1 * len2)

def get_recommendations_vecs():
    with open('modules/search_module/recommendation_vecs.pickle', 'rb') as handle:
        ''' Vector containing 
            [ listing_id: 
                [ 
                    "accommodates", 
                    'price', 
                    'latitude', 
                    'longitude', 
                    'review_scores_rating', 
                    'duration'
                ]
            ]
        '''
        return pickle.load(handle)

def get_calendar_availabilites(booked, year, month):
    ''' Get booking availablities for the next six months starting from current month '''
    all_dates = calendar.monthcalendar(year, month)
    for i in range(len(all_dates)):
        for j in range(7):
            curr_date = all_dates[i][j]
            if not all_dates[i][j]:  #

                all_dates[i][j] = {"date_number": None}
            else:
                all_dates[i][j] = {
                    "date_number": curr_date,
                    'available': curr_date not in booked,
                    'passed': datetime.now() > datetime(year, month, curr_date)
                }
    for i in range(6 - len(all_dates)):
        all_dates.append([{'date_number': None}] * 7)
    return all_dates