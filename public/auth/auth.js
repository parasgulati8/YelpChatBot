var MODE = "PROD"

function getUrlParam(paramKey) {
    let paramValue;
    window.location.href.replace(/[?#&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        if (key == paramKey) {
            paramValue = value
        }
    });
    return paramValue;
}

var id_token = getUrlParam('id_token');

if (!id_token) {
    if (MODE == "DEV") {
        window.location.href = "https://yelpchatbot.auth.us-east-1.amazoncognito.com/login?response_type=token&client_id=2g7m3euhabi15mnc17d8kkd6oj&redirect_uri=http://localhost:8000";
    } else if (MODE == "PROD") {
        window.location.href = "https://yelpchatbot.auth.us-east-1.amazoncognito.com/login?response_type=token&client_id=2g7m3euhabi15mnc17d8kkd6oj&redirect_uri=https://s3.amazonaws.com/findmyfood.webhost/index.html"
    } else {
        console.error("NO SUCH MODE: ", MODE)
    }
} else {
    AWS.config.region = 'us-east-1';
    AWS.config.credentials = new AWS.CognitoIdentityCredentials({
        IdentityPoolId: 'us-east-1:66442ebc-0d4a-4790-8055-3d9be2717436',
        Logins: {
            "cognito-idp.us-east-1.amazonaws.com/us-east-1_LUnGZFWnV": id_token
        }
    });
    var apigClient;
    AWS.config.credentials.refresh(() => {
        // var accessKeyId = AWS.config.credentials.accessKeyId;
        // var secretAccessKey = AWS.config.credentials.secretAccessKey;
        // var sessionToken = AWS.config.credentials.sessionToken;
        // console.log(accessKeyId);
        // console.log(secretAccessKey);
        // console.log(sessionToken);
        AWS.config.region = 'us-east-1';
        apigClient = apigClientFactory.newClient({
            accessKey: AWS.config.credentials.accessKeyId,
            secretKey: AWS.config.credentials.secretAccessKey,
            sessionToken: AWS.config.credentials.sessionToken, 
            region: 'us-east-1'
        });
    });
}

