import pyttsx3 as p
import speech_recognition as sr
from selenium_web import infow
from Yt_audio import music
from News import *
import randfacts
from jokes import *
from weather import *
import datetime

engine = p.init()

engine.setProperty('rate', 130)
voices = engine.getProperty('voices')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("Morning")
    elif hour>=12 and hour<=16:
        return("Afternoon")
    else:
        return("Evening")

today_date = datetime.datetime.now()
r = sr.Recognizer()

speak("Hello sir, good" + wishme() + "I am your voice assistant. ")
speak("Today is " + today_date.strftime("%d") + "of" + today_date.strftime("%B")+ "And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
speak("Temperature in new delhi is"+ str(temp()) + "degree celsius" + "and with" + str(des()))
speak("what can i do for you")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I am also having good day sir")
speak("what can i do for you?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening....")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("You need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("Searching {} in wikipedia".format(infor))
    print("Searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("you want me to play which video?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        video = r.listen(source)
        videoname = r.recognize_google(video)
    speak("Playing {} in Youtube".format(videoname))
    print("Playing {} in Youtube".format(videoname))
    assist = music()
    assist.play(videoname)

elif "news" in text2:
    print("Sure sir! Now I will read news for you.")
    speak("Sure sir! Now I will read news for you.")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("Sure Sir!")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that, " +x)

elif "joke" or "jokes" in text2:
    speak("Sure Sir, get ready for some chuckles")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
