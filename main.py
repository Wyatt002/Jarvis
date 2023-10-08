from datetime import datetime
import pyttsx3
from decouple import config


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

#Set Rate
engine.setProperty('rate', 190)

#Set Volume
engine.setProperty('volume', 1.0)

#Set Voice (Male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Text to Speech Conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Greet the user
def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 20):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I help you?")
