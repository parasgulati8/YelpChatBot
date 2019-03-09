import json

class UserDataFetcher:

    def __init__(self, event):
        self.event = event

    def fetchUserId(self):
        return self.event['requestContext']['authorizer']['claims']['custom:userId']

    def fetchUserRequestObject(self):
        print(self.event['body'])
        return json.loads(self.event['body'])

    def fetchUserMessage(self):
        return self.fetchUserRequestObject()['chatText']