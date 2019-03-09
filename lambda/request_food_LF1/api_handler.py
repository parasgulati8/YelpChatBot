import time
import os
import math
import logging

import intent_handler
from lambda_params import LambdaParams


LOGGER = logging.getLogger()

def lambda_handler(event, context):
    LOGGER.debug('event.bot.name={}'.format(event['bot']['name']))
    initTimeZone()
    lambdaParams = LambdaParams(event, context)
    return dispatch(lambdaParams)

def initTimeZone():
    os.environ['TZ'] = 'America/New_York'
    time.tzset()

def dispatch(lambdaParams):
    response = intent_handler.handle_intent(lambdaParams)
    print('Responding with: ', response)
    return response
    pass
