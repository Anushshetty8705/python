import pyttsx3
import pyjokes
import speech_recognition as sr
import pyaudio
import time
import webbrowser





def speechtxt():
    recognize=sr.Recognizer()
    with sr.Microphone( ) as source:
        print("listening...")
        txtspeech("listening")
        recognize.adjust_for_ambient_noise(source) #to remove background noise
        audio=recognize.listen(source)
        try:
            print("recognizing.....")
            txtspeech("recognizing")
            data=recognize.recognize_google(audio,language='en-in')
            return(data)
        except sr.UnknownValueError:
            return("neat age booglu...     ")
                     
          
             



def txtspeech(x):
    engine = pyttsx3.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ =='__main__':
 while True :
    questio=speechtxt()
    question=questio.lower()
    if "your name" in question:
        print(" my name is jalagara")
        txtspeech('my name is jalagara')
    elif "your girlfriend name" in question:
        print("my gf name is pavitra")
        txtspeech("my wife name is pavitra gowda")
    elif "your wife name" in question:
        print("my wife name is vijaylakshimi")
        txtspeech("my wife name is vijaylakshimi")
    elif "girlfriend and wife are " in question:
        print("akrama smabanda")
        txtspeech("akrama sambanda")
    elif "open "  in question:
        text=question.split()
        print(f"opening {text[1]}..")
        txtspeech(f"opening {text[1]}")
        webbrowser.open(f"https://{text[1]}.com/")
        print("waiting for 10 sec if u want to stop me plz tell exit when you hear lisiting")
        txtspeech("waiting for 10 sec if u want to stop me plz tell exit when you hear listing")
        time.sleep(10)
        continue
    elif "search "  in question:
        print("opening google..")
        txtspeech("opening google")
        webbrowser.open("https://www.google.co.in/")
        break
    elif "tell me a joke" in question:
        joke=pyjokes.get_joke(language="en")
        print(joke)
        txtspeech(joke)
    elif "today's date" in question:
        print(time.strftime(" today's date is \n %d/%m/%y"))
        txtspeech(time.strftime("today's date is %D"))
    elif "time now" in question:
        print(time.strftime("time is  \n%r"))
        txtspeech(time.strftime("time is %r "))
    elif "day is today" in question:
        print(time.strftime("today is   %a"))
        txtspeech(time.strftime("today is %a"))
    elif "exit" in question:
        print("thanku thanku \n exited")
        txtspeech("thanqou thanqou")
        exit()
    elif "neat" in question:
        print(question)
        txtspeech(question)
