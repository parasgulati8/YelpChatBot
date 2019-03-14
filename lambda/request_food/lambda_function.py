import json
import boto3
from UserDataFetcher import UserDataFetcher

cognitoClient = boto3.client('cognito-idp')
lexClient = boto3.client('lex-runtime')

def lambda_handler(event, context):

    userDataFetcher = UserDataFetcher(event)
    print(event)

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
            "Access-Control-Allow-Origin" : "*",
            "Allow" : "GET, OPTIONS, POST",
            "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
            "Access-Control-Allow-Headers" : "*"
         },
        'body': json.dumps(response["message"])
    }