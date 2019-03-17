$('#btn-input').keypress((event) => {
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
        onUserSendMessage()
    }
})

$('#btn-chat').click(() => {
    onUserSendMessage()
});

onUserSendMessage = () => {
    let userText = $('#btn-input').val();
    if (userText == "") {
        return
    }
    $('.msg_container_base').append(`
            <div class="row msg_container base_sent">
                <div class="col-md-10 col-xs-10">
                    <div class="messages msg_sent">
                        <p>` + userText + `</p>
                        <time datetime="2009-11-13T20:00">you . now</time>
                    </div>
                </div>
                <div class="col-md-2 col-xs-2 avatar">
                    <img src="resources/empty_dp.jpg" class=" img-responsive ">
                </div>
            </div>
    `);
    $('#btn-input').val('')
    animateIncomingMessage().then(() => {
        sendUserMessage(userText, (replyText) => {
            onReplyReceived(replyText)
        });
    })
}

onReplyReceived = (replyText) => {
    $('.msg_container_base').append(`
            <div class="row msg_container base_receive">
                <div class="col-md-10 col-xs-10">
                    <div class="messages msg_sent">
                        <p>` + replyText + `</p>
                        <time datetime="2009-11-13T20:00">chatbot . now</time>
                    </div>
                </div>
                <div class="col-md-2 col-xs-2 avatar">
                    <img src="http://www.bitrebels.com/wp-content/uploads/2011/02/Original-Facebook-Geek-Profile-Avatar-1.jpg" class=" img-responsive ">
                </div>
            </div>
    `);
    animateIncomingMessage()
}

function animateIncomingMessage() {
    $('#btn-input').val('')
    let msgContainer = $('.msg_container_base');
    msgContainer.animate({
        scrollTop: msgContainer[0].scrollHeight
    }, 300)
    return msgContainer.promise()
}

onReplyReceived('If you need some help, drop me a text!')