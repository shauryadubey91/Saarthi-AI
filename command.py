import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    print(voices)
    engine.say(text)
    engine.runAndWait()
   

def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=8, phrase_time_limit=7)

    try:
        print('recognizing')
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        eel.DisplayMessage(query) 
        speak(query) 
        time.sleep(2)
      

        return query.lower()

    except Exception:
        eel.DisplayMessage("Could not understand")
        return ""

@eel.expose
def allCommands():

    query = takecommand()
    print("Query:", query)

    if query is None or query == "":
        return

    if "open" in query:
        from AI.features import openCommand
        openCommand(query)

    elif "youtube" in query or query.startswith("play"):
        from AI.features import playYoutube
        playYoutube(query)


    else:
        print("not run")   
    
    eel.ShowHood()