console.log("controller.js loaded");

eel.expose(DisplayMessage);
eel.expose(ShowHood);

function DisplayMessage(message) {
    console.log("Message from Python:", message);

    $("#siriwave").attr("hidden", false);

    $(".siri-message li:first").text(message);

    $('.siri-message').textillate('stop');
    $('.siri-message').textillate('start');
}

function ShowHood(){
    $("#siriwave").attr("hidden", false);
}




$(document).ready(function(){

    // Start idle animation
    $('.ask-text').textillate({
        loop: true,
        in: { effect: 'fadeInUp' },
        out: { effect: 'fadeOutDown' },
        minDisplayTime: 1500
    });

    // Existing eel functions
    eel.expose(DisplayMessage);
    eel.expose(ShowHood);

    function DisplayMessage(message){
        $("#siriwave").attr("hidden", false);
        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('stop');
        $('.siri-message').textillate('start');
    }

    function ShowHood(){
        $("#siriwave").attr("hidden", false);
    }
});
