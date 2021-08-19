"""Use the google distance matrix web services API to print the
distance between two locations.

First cmd line arg is origin, second id destination, third is API key.
"""

from pprint import pprint
import requests
import sys


if __name__=="__main__":
    google_dist_api = "https://maps.googleapis.com/maps/api/distancematrix/json"
    resp = requests.get(google_dist_api,
                        params={"origins": [sys.argv[1]],
                                "destinations": [sys.argv[2]],
                                "mode": ["driving"],
                                "key": sys.argv[3]})

    pprint(resp.json())
