import json
import boto3

from UserDataFetcher import UserDataFetcher

lexClient = boto3.client('lex-runtime')

def lambda_handler(event, context):

    userDataFetcher = UserDataFetcher(event)

    response = lexClient.post_text(
        botName = "RestaurantDetailsFinder",
        botAlias = "$LATEST",
        userId = userDataFetcher.fetchUserId(),
        sessionAttributes = {},
        requestAttributes = {},
        inputText = userDataFetcher.fetchUserMessage()
    )

    return {
        'statusCode': 200,
        'headers': {
           "Access-Control-Allow-Origin": "*"
         },
        'body': json.dumps(response["message"])
    }