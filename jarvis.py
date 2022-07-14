import pyjoke
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
randVoice = random.randint(0, 1)
engine.setProperty('voice', voices[randVoice].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir ")
    else:
        speak("Good Evening Sir ")
    if randVoice == 0:
        speak("how may I help you")
    else:
        speak("how may I help you")


def takecommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login()


if __name__ == '__main__':
    # speak("Abhishek is a good boy")
    wishMe()
    while True:

        query = takecommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching on wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'who are you' in query:
            if randVoice == 0:
                speak("My name is Vision, your personal assistant")

            else:
                speak("My name is Friday, your personal assistant")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open_new("www.google.co.in")

        elif 'play music' in query:
            speak('playing')
            music_dir = 'D:\\Entertainment\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            randNo = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[randNo]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {strTime}")

        elif 'open telegram' in query:
            tele_path = "C:\\Users\\Abhishek\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(tele_path)

        elif 'open chrome' in query:
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        elif 'i love you' in query:
            speak("i love you too")

        elif 'on youtube' in query:
            speak("Tell the name of the song")
            s_yt = takecommand()
            pywhatkit.playonyt(s_yt)

        elif 'play' in query:
            query = query.replace('play', '')
            speak('playing' + query)
            pywhatkit.playonyt(query)

        elif 'email to abhishek' in query:
            try:
                speak("Enter the content")
                content = takecommand()
                to = "abhisheknamdeo97@yahoo.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry Sir email has not been sent due to an issue")

        elif 'who created you' in query:
            speak("I was created by Abhishek")

        elif ('stop' or 'exit' in query):
            speak("Thanks for interacting with me, have a great day ahead")
            exit()
