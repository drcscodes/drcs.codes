from pprint import pprint
import requests
import sys

def get_movie_data(query_params):
    ombd_api = 'http://www.omdbapi.com'
    resp = requests.get(ombd_api, params=query_params)
    return resp.json()


if __name__=='__main__':
    pprint(get_movie_data({'t': sys.argv[1], "apikey": sys.argv[2]}))
