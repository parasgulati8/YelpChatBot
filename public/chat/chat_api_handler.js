/*global WildRydes _config*/
    // $.ajax({
    //     method: 'POST',
    //     crossDomain: true,
    //     url: _config.api.invokeUrl + '/requestfood',
    //     data: JSON.stringify({
    //         chatText: message
    //     }),
    //     contentType: 'application/json',
    //     success: completeRequest,
    //     error: function ajaxError(jqXHR, textStatus, errorThrown) {
    //         console.error('Error requesting ride: ', textStatus, ', Details: ', errorThrown);
    //         console.error('Response: ', jqXHR.responseText);
    //         alert('An error occured when requesting your unicorn:\n' + jqXHR.responseText);
    //     }
    // });


sendUserMessage = (message, onReplyTextReceived) => {

        let params = {};
        let additionalParams = {};
        var body = {
            "chatText" : message
        }
        apigClient.chatbotPost(params, body, additionalParams)
        .then(function(result){
            console.log(result);
            onReplyTextReceived(result.data);
        }).catch( function(result){
            // Add error callback code here.
            console.error(result);
            onReplyTextReceived("Some error occured. Check console for details.");
        });

}

// Register click handler for #request button
$(function onDocReady() {
    
});



