

$('#btn-chat').click(()=> {
    var userText = $('#btn-input').val();
    $('.msg_container_base').append(`
            <div class="row msg_container base_sent">
                <div class="col-md-10 col-xs-10">
                    <div class="messages msg_sent">
                        <p>` + userText + `</p>
                        <time datetime="2009-11-13T20:00">Timothy • 51 min</time>
                    </div>
                </div>
                <div class="col-md-2 col-xs-2 avatar">
                    <img src="resources/empty_dp.jpg" class=" img-responsive ">
                </div>
            </div>
    `);
     $('#btn-input').val('')
     sendUserMessage(userText, (replyText)=>{
         onReplyReceived(replyText)
     });
});

onReplyReceived = (replyText) => {
    $('.msg_container_base').append(`
            <div class="row msg_container base_receive">
                <div class="col-md-10 col-xs-10">
                    <div class="messages msg_sent">
                        <p>` + replyText + `</p>
                        <time datetime="2009-11-13T20:00">Timothy • 51 min</time>
                    </div>
                </div>
                <div class="col-md-2 col-xs-2 avatar">
                    <img src="http://www.bitrebels.com/wp-content/uploads/2011/02/Original-Facebook-Geek-Profile-Avatar-1.jpg" class=" img-responsive ">
                </div>
            </div>
    `);
     $('#btn-input').val('')
}