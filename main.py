import eel
from AI.features import playAssistantsound
from AI.command import allCommands

eel.init("www")

@eel.expose
def play_sound():
    playAssistantsound()

eel.start("index.html", mode="chrome", port=8000, block=False)

while True:
    eel.sleep(1)


