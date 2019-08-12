import time

import boto3

from modules.database_module.models import Listing
from modules.database_module.shared_db import db
from modules.shared_methods import get_user, sanitize_dict_keys
from modules.google_api import Googlemap_api

import os

gmap_api = Googlemap_api()

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

bucket_name = os.environ.get('bucket_name')
s3 = boto3.client(
   "s3",
   aws_access_key_id=AWS_ACCESS_KEY_ID,
   aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def sanitize_listings(listings):
    ''' Filter out metadata keys in each listing '''
    ret = []
    if listings:
        ret = [ sanitize_dict_keys(booking) for booking in listings ]
    return ret

def get_coordinates(address):
    ''' Use google maps API to identify a location's coordinates '''
    try:
        location = gmap_api.geo_loc_from_text(address)
        return location['lng'], location['lat']
    except:
        print('Location could not be found')
        return None, None

def preprocess_amenities(amenities):
    ''' Format the amenities the same way as in DialogFlow '''
    amenities = amenities.split(',')
    quoted = [ f'"{amenity}"' for amenity in amenities ]
    formatted = '{' + ','.join(quoted) + '}'
    return formatted

def generate_img_uri(request):
    ''' Upload an image to AWS S3 then generate a URI for it to store in the picture_url field '''

    # default image URI
    default_img = 'http://thechurchontheway.org/wp-content/uploads/2016/05/placeholder1.png'
    
    img_uri = default_img

    if 'picture_obj' in request.files:
        try: 
            # Extract image fil object from request
            image = request.files['picture_obj']
            # Generate a unique file name for image
            # based on the user ID, num. listings and current time
            user_id = get_user(request)
            num_listings = db.session.query(Listing).filter_by(host_id=user_id).count()
            image_name = f"user-{user_id}-listing-{num_listings}-{str(int(time.time()))}"
            # Upload image to S3
            s3.upload_fileobj(image, bucket_name, image_name, ExtraArgs={ 'ACL': 'public-read', 'ContentType': image.mimetype })
            # Create URI
            img_uri = f"https://s3-ap-southeast-2.amazonaws.com/{bucket_name}/" + image_name
            print("Image saved:", img_uri)
        except Exception as e:
            print("image not saved")
            print(e)

    return img_uri