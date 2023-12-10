import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import pyttsx3
import wikipedia

listener = sr.Recognizer()
engine=pyttsx3.init()

voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print('Listening.........')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if "google" in command:
                command = command.replace("google","")

    except:
        pass
    return command

def run_assistant():
    command=get_command()

    if 'play' in command:
        song=command.replace("play",'')
        talk("Playing"+song)
        pywhatkit.playonyt(song)
        print("Playing song")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M %p")
        talk("Now time is "+time)
    elif "tell me about" in command:
        about=command.replace("tell me about","")
        info=wikipedia.summary(about,2)
        print(info)
        talk(info)
    elif "joke" in command:
        joke1=pyjokes.get_joke()
        print(joke1)
        talk(joke1)
    else:
        talk("sorry i can't understand tell me again")

while True:
    run_assistant()







