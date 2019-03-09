import lambda_function

if __name__ == "__main__":
    event = {
        'requestContext': {
            'authorizer': {
                'claims': {
                    'custom:userId' : 'randomStringHere'
                }
            }
        },
        'body': '{ "chatText" : "hello friend" }'

    }
    context = {}
    response = lambda_function.lambda_handler(event, context)
    print(response)