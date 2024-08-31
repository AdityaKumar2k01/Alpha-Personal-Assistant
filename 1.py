import pyttsx3 
import speech_recognition as sr #

import datetime
import wikipedia   
import webbrowser
import os  
import urllib  
from gmail.gmail import gmail
import sys
import smtplib
import getpass
from pytube import YouTube 
import pyautogui
import cv2


engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.0)
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Aditya")
    elif hour>=12 and hour<16:
        speak("Good afternoon Aditya")
    else:
        speak("Good Evening Aditya")
    
    print("Hello sir I am Alpha Your Personal Assistant ")
    speak("Hello sir I am Alpha Your Personal Assistant ")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Listening.....")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)

        print("say that again please....")
        return "None"
    return query
if __name__=="__main__":
    
    wishme()

    while True:
        query=takecommand().lower() 
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open camera' in query:
            vidcap = cv2.VideoCapture("D:\danil file\KULIAH\test.mp4")
            count = 0 
            while vidcap.isOpened():
                ret, image = vidcap.read()
                if ret == True: 
                    cv2.imwrite('D:\SONG' % count, image )
                    count+=1
                else:
                    break



        elif 'alpha are you there' in query:
            print("Yes Sir, at your service")
            speak("Yes Sir, at your service")


        elif 'alpha who made you' in query:
            print("Aditya build me in AI")
            speak("Aditya build me in AI")


        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open youtube' in query:

            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")


        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'screenshot' in query:
            speak("taking screenshot")
            music_dir='D:\SONG'
            screenshot=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            screenshot()


        elif 'open kiit' in query:
            webbrowser.open("kiit.ac.in/sap/")

            


        elif 'open aditya' in query:
            webbrowser.open("adityakumar2k01.github.io/Portfolioadi/") 


        elif 'open proptrack' in query:
            webbrowser.open("/proptrack.herokuapp.com/")   

        
        elif 'play music' in query:
            music_dir='D:\SONG'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif 'what is the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        

        else:
              print("Sorry Sir It is not in my system. Can i do anything else for you ?")
              speak("Sorry Sir It is not in my system. Can i do anything else for you ?")




    
    

             
        
    
            

    

