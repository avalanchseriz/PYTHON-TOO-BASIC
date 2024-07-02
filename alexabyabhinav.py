import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

whomademe = "abhinav harsh"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
cred = "this program was a self logic by abhinav harsh....."


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'serizen' in command:
                command = command.replace('serizen', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    if "shutdown" in command:
            talk("do you want to shut down")
            z = input("y to shut down: ")
            if z == "Y" or "y":
                talk("shutting down")
                os.system('shutdown -s')
            else:
                talk("shutdown canceled")
    elif "denying" in command:
        os.system('shutdown -a')
        talk("shutdown canceled")
    elif 'credits' in command:
        print(cred)
        talk(cred)
    elif 'who am' in command:
       print(whomademe)
       talk(whomademe)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command or 'who was' in command:
        try:
            person = command.replace('who is', '').replace('who was', '').strip()
            print("Querying Wikipedia for:", person)
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            print("It seems there are multiple interpretations of the term. Please be more specific.")
            talk("It seems there are multiple interpretations of the term. Please be more specific.")
        except wikipedia.exceptions.PageError as e:
            print("Sorry, I couldn't find information about that.")
            talk("Sorry, I couldn't find information about that.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()