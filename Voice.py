from gtts import gTTS
import playsound
import datetime
import speech_recognition as sr
import os

def set_pas():
    pas = "train"
    return pas

def speak(text):
    tts = gTTS(text=text, lang="en-in", slow=False)
    filename = "voice1.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")


def accept():

    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("listening...")
        audio = r.listen(source)
        r.energy_threshold = 10

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        speak("Say that again please! ")
        return "NONE"

    return query