import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install pip install SpeechRecognition #pip install pipwin  #pipwin install pyaudio
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os






engine = pyttsx3.init('espeak')  # sapi5 is for windows and espeak for ubuntu
#voice=engine.getProperty('voices') #works only with windows
#engine.setProperty('voice',voice[0].id) #works only with windows
# engine.setProperty('voice', 'english_rp+f5')  # changes voice to female(mostly for ubuntu)
engine.setProperty('rate', 200)





def speak(audio):
    engine.say(audio)

    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(day)
    speak(month)
    speak(year)


def wishme():
    hour = datetime.datetime.now().hour
    if 6 <= hour <= 11:
        speak("Good Morning!")
    elif 12 <= hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Night")

    speak("Welcome back Sir")
    speak("Jarvis your assistant. How can I help?")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)

    except Exception as e:
        print(e)
        speak("Sorry! I don't know how to help with that!")
        return "None"
    return query

def sendMail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()                               #Identify yourself to an ESMTP server using EHLO
    server.starttls()
    server.login("test@gmail.com","@test$")
    server.sendmail("test@gmail.com",to,content)
    server.close()


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak('Searching in wikipedia')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)

        elif ("my name" or "who i am") in query:
            speak('You are my boss Mr.Vikas')

        elif ("tata" in query) or ("Bye" in query) or ("shut up" in query) or ("exit" in query)  :
            speak("Signing Off!")
            quit()
        elif "send a mail" in query:
            try:
                speak("What should I write")
                content = takeCommand()
                print(content)
                speak("To whom I should write")
                to = "test2@gmail.com"
                sendMail(to,content)
                speak("Mail sent")
            except Exception as e:
                print(e)
                speak("failed!")
        elif "on chrome" in query:
            speak("What should I search.")
            chromepath ="/usr/bin/google-chrome %s"             #find suitable chromepath for your OS
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)

        elif ("vlcplayer" in query) or ("vlc" in query) or ("video player" in query) or ("vlcplayer" in query):
            speak("Opening")
            speak("VLC PLAYER")
            os.system("VLC")
        else:
            speak("bye")

