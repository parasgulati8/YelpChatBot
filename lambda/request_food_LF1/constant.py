
class GreetingIntent:
    REPLY_1 = "Hello. How may I help you?"

class DiningSuggestionsIntent:
    SLOT_NAMES = ['Cuisine', 'Location', 'PartyPeople', 'Date', 'Time']
    SLOT_NAME_LOCATION = 'Location'
    SLOT_NAME_CUISINE = 'Cuisine'
    SLOT_NAME_PARTY_PEOPLE = 'PartyPeople'
    SLOT_NAME_DATE = 'Date'
    SLOT_NAME_TIME = 'Time'

    VALID_CUISINES_UPPERCASE = ['THAI', 'INDIAN', 'CHINESE', 'ITALIAN', 'MEXICAN', 'JAPANESE']
    VALID_LOCATIONS_UPPERCASE = ['BROOKLYN', 'MANHATTAN', 'QUEENS', 'BRONX', 'STATEN ISLAND']
    VALID_MAX_PARTY_PEOPLE = 10
    VALID_MIN_PARTY_PEOPLE = 1

    SLOT_ELICIT_RESPONSES = {
        SLOT_NAME_LOCATION : 'Where are you looking for the restaurants?',
        SLOT_NAME_CUISINE : 'Which cuisine would you prefer?',
        SLOT_NAME_PARTY_PEOPLE : 'How many people?',
        SLOT_NAME_DATE: 'Which date are you looking for?',
        SLOT_NAME_TIME: 'Which time are you looking for?'
    }

    SLOT_INVALID_RESPONSES = {
        SLOT_NAME_LOCATION: 'I`m sorry. The only available locations are Brooklyn, Manhattan, Qeeens, Bronx and Staten Island. Can you try again?',
        SLOT_NAME_CUISINE: 'I`m sorry. Only available cuisines are thai, indian, chinese, italian, mexican and japanese. Can you try again?',
        SLOT_NAME_PARTY_PEOPLE: 'I`m sorry number of people must be atleast 1 and less than 10. Can you try again?',
        SLOT_NAME_DATE: 'I`m sorry you can`t have a date in the past. Can you try again?',
        SLOT_NAME_TIME: 'I`m sorry that seems to be an invalid response. Can you try again?'
    }

    SLOT_VALIDATE_SUCCESS_RESPONSE = 'Alright. Please wait while I fetch some suggestions for you.'

    YELP_API_KEY = "0EbA0ZINSb_iiHd_YB2EvHir88SKMFC3fAEyC9gRP5HByf_l5-daiRvcTOTNFyhWFBJhgEOlqezAdwgrlhmvnxYYrWHBVz9j3yZj3TsKgHcmsBBDUkidhfHI8258XHYx"
    YELP_API_URL_TEMPLATE = "https://api.yelp.com/v3/businesses/search?term=Restaurants&location=@LOCATION&categories=@CATEGORY&limit=@LIMIT&sort_by=best_match"
    YELP_API_URL_PARAM_LOCATION = "@LOCATION"
    YELP_API_URL_PARAM_CATEGORY = "@CATEGORY"
    YELP_API_URL_PARAM_LIMIT = "@LIMIT"
    
    YELP_API_RESPONSE_JSON_BUSINESS = "businesses"
    YELP_API_RESPONSE_JSON_NAME="name"
    YELP_API_RESPONSE_JSON_LOCATION="location"
    YELP_API_RESPONSE_JSON_DISPLAYADDRESS="display_address"


    class CodeHooks:
        DIALOG_CODE_HOOK = 'DialogCodeHook'
        FULFILMENT_CODE_HOOK = 'FulfillmentCodeHook'


class IntentNames:
    DINING_SUGGESTIONS_INTENT = "DiningSuggestionsIntent"
    GREETING_INTENT = "GreetingIntent"