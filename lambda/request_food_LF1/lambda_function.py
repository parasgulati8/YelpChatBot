import json
import dateutil.parser
import datetime
import time
import os
import math
import random
import logging 

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
            
        }
    }
    
def parse_int(n):
    try:
        return int(n)
    except ValueError:
        return float('nan')

def build_validation_result(is_valid, violated_slot, message_content):
    return {
        'isValid': is_valid,
        'violatedSlot': violated_slot,
        'message': {'contentType': 'PlainText', 'content': message_content}
    }
    
def validate_restaurant_slots(location,cuisine,numberofpeople,date,time):
    """ --- check location in US city???---"""

    if time:
        if len(time) != 5:
            return build_validation_result(False, 'Time', 'I did not recognize that, what time would you like to book your reservation?')

        hour, minute = time.split(':')
        hour = parse_int(hour)
        minute = parse_int(minute)
        if math.isnan(hour) or math.isnan(minute):
            return build_validation_result(False, 'Time', 'I did not recognize that, what time would you like to book your reservation?')

        if hour < 10 or hour > 23:
            # Outside of business hours
            return build_validation_result(False, 'Time', 'The restaurants usually serves from 10 am to 11 pm.  What time works best for you?')
        if hour == 23 and minute>0:
            # Outside of business hours
            return build_validation_result(False, 'Time','The restaurants dont serve after  11 pm.What time works for you before?')
        
    return build_validation_result(True, None, None)
   
""" --- Intents --- """

def dining_suggestion(intent_request):
    """
    Performs dialog management and fulfillment for finding restaurants suggestion.
    Beyond fulfillment, the implementation for this intent demonstrates the following:
    1) Use of elicitSlot in slot validation and re-prompting
    2) Use of confirmIntent to support the confirmation of inferred slot values, when confirmation is required
    on the bot model and the inferred slot values fully specify the intent.
    """
    location = intent_request['currentIntent']['slots']['Location']
    cuisine = intent_request['currentIntent']['slots']['Cuisine']
    numberofpeople = intent_request['currentIntent']['slots']['PartyPeople']
    date = intent_request['currentIntent']['slots']['Date']
    time = intent_request['currentIntent']['slots']['Time']
    source = intent_request['invocationSource']
    output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
    

    if source == 'DialogCodeHook':
        # Perform basic validation on the supplied input slots.
        slots = intent_request['currentIntent']['slots']
        validation_result = validate_restaurant_slots(location,cuisine,numberofpeople,date,time)
        logger.debug(location)
        logger.debug(validation_result)
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                slots,
                validation_result['violatedSlot'],
                validation_result['message']
            )
        if not cuisine:
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                intent_request['currentIntent']['slots'],
                'Cuisine',
                {'contentType': 'PlainText', 'content': 'Which cuisine would you prefer?'}
        
            )
        if not location:
            logger.debug(validation_result)
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                intent_request['currentIntent']['slots'],
                'Location',
                {'contentType': 'PlainText', 'content': 'Where are you looking for the restaurants?'},
            )
        if not numberofpeople:
            logger.debug(validation_result)
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                intent_request['currentIntent']['slots'],
                'Location',
                {'contentType': 'PlainText', 'content': 'How many people?'},
            )



def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'DiningSuggestionsIntent':
        return dining_suggestion(intent_request)
    if intent_name == 'GreetingIntent':
        return
    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """

def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
   
    return dispatch(event)