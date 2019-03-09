import constant
from botocore.vendored import requests
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode

def suggest_restaurants(cuisine, location, party_people, date, time):
    return request_yelp_suggestions(cuisine, location)


def request_yelp_suggestions(category, location):
    headers = {
        'Authorization': 'Bearer %s' %constant.DiningSuggestionsIntent.YELP_API_KEY,
    }
    url = constant.DiningSuggestionsIntent.YELP_API_URL_TEMPLATE.replace(
        constant.DiningSuggestionsIntent.YELP_API_URL_PARAM_LOCATION, location
    ).replace(
        constant.DiningSuggestionsIntent.YELP_API_URL_PARAM_CATEGORY, category
    ).replace(
        constant.DiningSuggestionsIntent.YELP_API_URL_PARAM_LIMIT, '5'
    )
    request_type = 'GET'

    response = requests.request(request_type, url, headers=headers)

    return str(response.json())

