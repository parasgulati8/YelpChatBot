import constant
import suggestion_api
from lambda_params import LambdaResponse
import datetime

def handle_intent(lambdaParams):
    intent_name = lambdaParams.get_requested_intent_name()

    if intent_name == constant.IntentNames.GREETING_INTENT:
        return handle_greeting_intent(lambdaParams)

    if intent_name == constant.IntentNames.DINING_SUGGESTIONS_INTENT:
        return handle_dining_suggestion_intent(lambdaParams)

    raise AssertionError('Intent with name ' + intent_name + ' not supported')


def handle_greeting_intent(lambdaParams):
    return constant.GreetingIntent.REPLY_1


def handle_dining_suggestion_intent(lambdaParams):
    # 1. Validate slots
    # 2. Fulfill Request
    helpers = DiningSuggestionIntentHelpers(lambdaParams)
    if lambdaParams.get_invocation_source() == constant.DiningSuggestionsIntent.CodeHooks.DIALOG_CODE_HOOK:
        return helpers.handle_dialog_code_hook()
    elif lambdaParams.get_invocation_source() == constant.DiningSuggestionsIntent.CodeHooks.FULFILMENT_CODE_HOOK:
        return helpers.handle_fulfilment_code_hook()
    else:
        raise AssertionError('No such code hook is being handled')


class DiningSuggestionIntentHelpers:

    def __init__(self, lambdaParams):
        self.lambdaParams = lambdaParams

    def handle_dialog_code_hook(self):
        for slot_name in constant.DiningSuggestionsIntent.SLOT_NAMES:
            slot_value = self.lambdaParams.get_slots()[slot_name]
            if not slot_value:    # If slot is not present, elicit that slot
                return self.build_elicit_slot_response(slot_name, constant.DiningSuggestionsIntent.SLOT_ELICIT_RESPONSES[slot_name])
            else:   # If slot is present, but is invalid, elicit that slot again
                print(slot_name, self.lambdaParams.event)
                if slot_name == constant.DiningSuggestionsIntent.SLOT_NAME_CUISINE:
                    if not self.is_valid_cuisine():
                        return self.build_elicit_slot_response(slot_name, constant.DiningSuggestionsIntent.SLOT_INVALID_RESPONSES[slot_name])

                if slot_name == constant.DiningSuggestionsIntent.SLOT_NAME_LOCATION:
                    if not self.is_valid_location():
                        return self.build_elicit_slot_response(slot_name, constant.DiningSuggestionsIntent.SLOT_INVALID_RESPONSES[slot_name])

                if slot_name == constant.DiningSuggestionsIntent.SLOT_NAME_PARTY_PEOPLE:
                    if not self.is_valid_party_people():
                        return self.build_elicit_slot_response(slot_name, constant.DiningSuggestionsIntent.SLOT_INVALID_RESPONSES[slot_name])

                if slot_name == constant.DiningSuggestionsIntent.SLOT_NAME_DATE:
                    if not self.is_valid_date():
                        return self.build_elicit_slot_response(slot_name, constant.DiningSuggestionsIntent.SLOT_INVALID_RESPONSES[slot_name])

                if slot_name == constant.DiningSuggestionsIntent.SLOT_NAME_TIME:
                    if not self.is_valid_time():
                        return self.build_elicit_slot_response(slot_name, constant.DiningSuggestionsIntent.SLOT_INVALID_RESPONSES[slot_name])

        # If everything is valid, return all success response
        lambdaResponse = LambdaResponse()
        return lambdaResponse.delegate(self.lambdaParams.get_session_attributes(), self.lambdaParams.get_slots())

    def build_elicit_slot_response(self, slot_name, slot_message):
        lambdaResponse = LambdaResponse()
        return lambdaResponse.elicit_slot(
            self.lambdaParams.get_session_attributes(),
            self.lambdaParams.get_requested_intent_name(),
            self.lambdaParams.get_slots(),
            slot_name,
            slot_message
        )

    def is_valid_cuisine(self):
        return self.lambdaParams.get_slots()[constant.DiningSuggestionsIntent.SLOT_NAME_CUISINE].upper() in constant.DiningSuggestionsIntent.VALID_CUISINES_UPPERCASE

    def is_valid_location(self):
        return self.lambdaParams.get_slots()[constant.DiningSuggestionsIntent.SLOT_NAME_LOCATION].upper() in constant.DiningSuggestionsIntent.VALID_LOCATIONS_UPPERCASE

    def is_valid_party_people(self):
        return constant.DiningSuggestionsIntent.VALID_MIN_PARTY_PEOPLE \
                    <= int(self.lambdaParams.get_slots()[constant.DiningSuggestionsIntent.SLOT_NAME_PARTY_PEOPLE])\
                        <= constant.DiningSuggestionsIntent.VALID_MAX_PARTY_PEOPLE

    def is_valid_date(self):
        dateString = self.lambdaParams.get_slots()[constant.DiningSuggestionsIntent.SLOT_NAME_DATE]
        date = datetime.datetime.strptime(dateString, "%Y-%m-%d")
        return date.date() >= datetime.date.today()

    def is_valid_time(self):
        return True

    def handle_fulfilment_code_hook(self):
        lambdaResponse = LambdaResponse()
        return lambdaResponse.success(
            self.lambdaParams.get_session_attributes(),
            suggestion_api.suggest_restaurants(
                self.lambdaParams.get_slots()[constant.DiningSuggestionsIntent.SLOT_NAME_CUISINE],
                self.lambdaParams.get_slots()[constant.DiningSuggestionsIntent.SLOT_NAME_LOCATION],
                self.lambdaParams.get_slots()[constant.DiningSuggestionsIntent.SLOT_NAME_PARTY_PEOPLE],
                self.lambdaParams.get_slots()[constant.DiningSuggestionsIntent.SLOT_NAME_DATE],
                self.lambdaParams.get_slots()[constant.DiningSuggestionsIntent.SLOT_NAME_TIME]
            )
        )

