
class LambdaParams:

    def __init__(self, event, context):
        self.event = event
        self.context = context

    def get_requested_intent_name(self):
        return self.event['currentIntent']['name']

    def get_slots(self):
        return self.event['currentIntent']['slots']

    def get_invocation_source(self):
        return self.event['invocationSource']

    def get_session_attributes(self):
        return self.event['sessionAttributes']


class LambdaResponse:

    def elicit_slot(self, session_attributes, intent_name, slots, slot_to_elicit, message):
        return {
            'sessionAttributes': session_attributes,
            'dialogAction': {
                'type': 'ElicitSlot',
                'intentName': intent_name,
                'slots': slots,
                'slotToElicit': slot_to_elicit,
                'message': {'contentType': 'PlainText', 'content': message}

            }
        }

    def delegate(self, session_attributes, slots):
        return {
            'sessionAttributes': session_attributes,
            'dialogAction': {
                'type': 'Delegate',
                'slots': slots
            }
        }

    def success(self, session_attributes, message):
        return {
            'sessionAttributes': session_attributes,
            'dialogAction': {
                'type': 'Close',
                'fulfillmentState': 'Fulfilled',
                'message': {'contentType': 'PlainText', 'content': message}
            }
        }