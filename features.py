
import pygame
import os
import re
import pywhatkit as kit
from AI.command import speak
from AI.config import ASSISTANT_NAME



pygame.mixer.init()

def playAssistantsound():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file = os.path.join(base_dir, "..", "www", "asset", "vindore", "Texllate", "audio", "start_sound.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


import webbrowser

def openCommand(query):
    query = query.lower().strip()

       # ---- Websites ----
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "instagram": "https://www.instagram.com/im_shxurya",
        "whatsapp": "https://web.whatsapp.com",
        "github": "https://github.com/shauryadubey91",
        "linkedin": "https://www.linkedin.com/in/saurya-dubey-435645395",
        "snapchat": "https://www.snapchat.com/shauryadubey20",
        "pickachu": "https://8-02-2026.netlify.app/",
        "pikachu": "https://8-02-2026.netlify.app/"
    }

    # ---- Apps ----
    apps = {
        "notepad": "notepad",
        "calculator": "calc",
        "paint": "mspaint",
        "vlc": r"C:\Users\Shaurya\Videos"
    }

    # ---- VS Code Path ----
    vscode_path = r"C:\Users\Shaurya\AppData\Local\Programs\Microsoft VS Code\Code.exe"

    # Open websites
    for site in sites:
        if site in query:
            speak(f"Opening {site}")
            webbrowser.open(sites[site])
            return

    # Open system apps
    for app in apps:
        if app in query:
            speak(f"Opening {app}")
            os.system(apps[app])
            return
        
    # open video
    if "video" in query:
        speak("Playing video")
        video_folder = r"C:\Users\Shaurya\Videos"

    for file in os.listdir(video_folder):
        if file.endswith((".mp4", ".mkv", ".avi")):
            os.startfile(os.path.join(video_folder, file))
            return

    # Open VS Code
    if "code" in query or "vs code" in query:
        if os.path.exists(vscode_path):
            speak("Opening Visual Studio Code")
            os.startfile(vscode_path)
            return
        else:
            speak("VS Code not found")

    speak("Application not found")

def playYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    command = command.lower()

    # remove assistant name if present
    command = command.replace("saarthi", "")

    # remove keywords
    command = command.replace("saarthi", "")
    command = command.replace("play", "")
    command = command.replace("on youtube", "")
    command = command.replace("youtube", "")

    return command.strip()
