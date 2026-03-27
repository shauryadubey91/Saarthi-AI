$(document).ready(function () {

  // Siri Wave Init
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 600,
    height: 150,
    style: "ios9",
    amplitude: 1,
    speed: 0.30,
    autostart: true
  });

  console.log("main.js loaded");

  $("#MicBtn").click(function () {
      console.log("Mic clicked");

      $("#siriwave").attr("hidden", false);
      $(".ring").hide();
      $("h5").hide();

      eel.play_sound();      
      eel.allCommands();     
  });

});
