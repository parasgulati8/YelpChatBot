
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
    VALID_LOCATIONS_UPPERCASE = ['BROOKLYN', 'MANHATTAN']
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
        SLOT_NAME_LOCATION: 'I`m sorry. The only available locations are Brooklyn and Manhattan',
        SLOT_NAME_CUISINE: 'I`m sorry. Only available cuisines are that, indian, chinese, italian, mexican and japanese',
        SLOT_NAME_PARTY_PEOPLE: 'I`m sorry number of people must be atleast 1 and less than 10',
        SLOT_NAME_DATE: 'Which date are you looking for?',
        SLOT_NAME_TIME: 'Which time are you looking for?'
    }

    SLOT_VALIDATE_SUCCESS_RESPONSE = 'Alright. Please wait while I fetch some suggestions for you.'

    YELP_API_KEY = "0EbA0ZINSb_iiHd_YB2EvHir88SKMFC3fAEyC9gRP5HByf_l5-daiRvcTOTNFyhWFBJhgEOlqezAdwgrlhmvnxYYrWHBVz9j3yZj3TsKgHcmsBBDUkidhfHI8258XHYx"
    YELP_API_URL_TEMPLATE = "https://api.yelp.com/v3/businesses/search?term=Restaurants&location=@LOCATION&categories=@CATEGORY&limit=@LIMIT&sort_by=best_match"
    YELP_API_URL_PARAM_LOCATION = "@LOCATION"
    YELP_API_URL_PARAM_CATEGORY = "@CATEGORY"
    YELP_API_URL_PARAM_LIMIT = "@LIMIT"


    class CodeHooks:
        DIALOG_CODE_HOOK = 'DialogCodeHook'
        FULFILMENT_CODE_HOOK = 'FulfillmentCodeHook'


class IntentNames:
    DINING_SUGGESTIONS_INTENT = "DiningSuggestionsIntent"
    GREETING_INTENT = "GreetingIntent"