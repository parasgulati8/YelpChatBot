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

    response = requests.request(request_type, url, headers = headers)
   
    data = response.json()

    restaurants=[]
    for business in data[constant.DiningSuggestionsIntent.YELP_API_RESPONSE_JSON_BUSINESS]:
        restaurant = {}
        restaurant["name"] = business[constant.DiningSuggestionsIntent.YELP_API_RESPONSE_JSON_NAME]
        location = ""
        for address in business[constant.DiningSuggestionsIntent.YELP_API_RESPONSE_JSON_LOCATION][constant.DiningSuggestionsIntent.YELP_API_RESPONSE_JSON_DISPLAYADDRESS]:
            location = location +" ,"+ address
        restaurant["location"] = location
        
        restaurants.append(restaurant)

    endstring = ''
    for i in range(1, len(restaurants)):
        str_each = str(i) + ". "+restaurants[i]["name"]+restaurants[i]["location"]+ ";\n"
        endstring += str_each

    print(endstring)
    endstring="Here are my suggestions for you "+endstring+" Enjoy your meal!!"
    return endstring

