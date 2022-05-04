import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime



listener = sr.Recognizer()
engine = pyttsx3.init()

#Switch to a female voice... Because It sounds better

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

#The Speech recognition system won't work unless the word 'ada' is mentioned

def listen_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ada' in command:
                command = command.replace('ada', '')
                print(command)
    except:
        pass
    return command


def run_ada():
    command = listen_command()
    
    print(command)
    
    #Play a song on Youtube

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is ' + time)
    elif 'search for' in command:
        content = command.replace('search for', '')

        # 1 refers to the number of sentences printed and read from the original Wikipedia text 

        info = wikipedia.summary(content, 1)
        print(info)
        talk(info)
    else:
        talk('Please say the command again.')


while True:
    run_ada()