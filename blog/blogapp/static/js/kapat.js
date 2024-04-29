setTimeout(function() {
    var messageList = document.getElementById("messageList");
    if (messageList) {
        messageList.parentNode.removeChild(messageList);
    }
}, 1000);