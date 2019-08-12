import googlemaps
import time
from googleplaces import GooglePlaces
from pprint import pprint
import os

class Googlemap_api:
    
    def __init__(self, key = os.environ.get("gmaps_key") ):

        if not key:
            raise Exception("Key required for Google maps client")

        self.gmaps = googlemaps.Client(key=key)


    def geo_loc_from_text(self, text_address):
        '''
        :param text_address: an text form sting address
        :return: {lat: , lng: }
        '''
        # Geocoding an address
        geocode_result = self.gmaps.geocode(text_address)
        return geocode_result[0]['geometry']['location']


    def text_loc_from_geo(self, geo_loc):
        '''

        :param geo_loc: a tutple with latitude and longitude
        :return: a text form address
        '''
        # Look up an address with reverse geocoding
        reverse_geocode_result = self.gmaps.reverse_geocode(geo_loc)
        return reverse_geocode_result[0]['address_components'][1]['long_name']


    def distance(self, origin, destination, mode='walking'):
        if type(origin) is str:
            origin = self.geo_loc_from_text(origin)
        if type(destination) is str:
            destination = self.geo_loc_from_text(destination)
        result = self.gmaps.distance_matrix(origins = origin, destinations = destination, mode = mode)
        pprint(result)
        dist_km = result['rows'][0]['elements'][0]['distance']['value']/1000
        time_duration = result['rows'][0]['elements'][0]['duration']['text']
        return dist_km, time_duration


    def nearby_search(self, location, type_of, distance =200, topK = 5, keyword=None):
        '''
        see developer document
        :param location:
        :param distance:
        :param type:
        :param keyword:
        :return:
        '''
        re_len = 0
        token =''
        if type(location) is str:
            geo_loc = self.geo_loc_from_text(location)
            result = self.gmaps.places_nearby(geo_loc, radius=distance, type=type_of, keyword=keyword)
            try:
                token = result['next_page_token']
            except:
                pass
            re_len = len(result['results'])
            while token:
                time.sleep(2)
                result = result = self.gmaps.places_nearby(page_token = token)
                try:
                    token = result['next_page_token']
                except:
                    token = ''
                re_len += len(result['results'])

        else:
            result = self.gmaps.places_nearby(location, radius = distance, type=type_of, keyword = keyword, page_token = token)# rank_by = 'distance')
            try:
                token = result['next_page_token']
            except:
                pass
            re_len = len(result['results'])
            while token:
                time.sleep(2)
                result = result = self.gmaps.places_nearby(location, radius=distance, type=type_of, keyword=keyword, \
                                                           page_token=token)
                try:
                    token = result['next_page_token']
                except:
                    token = ''
                re_len += len(result['results'])

        list_of_results = []
        return re_len


    def return_nearby(self, location, distance =200, keyword =None):
        type_of = ['ATM', 'cafe', 'bar', 'restaurant', 'bus_station', 'park', 'park', 'train_station']
        places = {'ATM':0, 'cafe':0, 'bar':0, 'restaurant':0, 'bus_station':0, 'park':0, 'train_station':0}
        for t in type_of:
            num_of_places = self.nearby_search(location, t, distance)
            places[t] = num_of_places

        return places
