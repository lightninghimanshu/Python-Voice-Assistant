import pyfiglet
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import subprocess as sp
import pywhatkit
import requests
import matplotlib.pyplot as plot
import math
from tqdm import tqdm
import time


#initialising text to speech library
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#setting the voice
engine.setProperty('voice', voices[0].id)


#loading bar for mathbot
def loading(string):
    for i in tqdm (range (101), 
                desc=string,
                ascii=False, ncols=75):
        time.sleep(0.01)
        
    print("Complete.")


#mathbot code
def mathbot():
    loading("Turning into MATH ness")
    print("TRANSITION COMPLETE ✅")
    print("I can solve some of yours Mathematical Problems")
    print("Since the programme is still in development, please input one command at a time.")
    while True:
        try:
            z=0
            sp = returnCommand().lower()
            print('\033[1m'+"User:"+'\033[0m', sp.capitalize())
            print('\033[1m'+"Bot:"+'\033[0m', end=" ")
            nos = [int(i) for i in sp.split() if i.isdigit()]
            if "how are you" in sp:
                z = 1
                print("I'm fine, How can I help you?")
                speak("I'm fine, How can I help you?")
            if sp == "hi" or "hello" in sp:
                z = 1
                print("Hello, How can I help you?")
                speak("Hello, How can I help you?")
            if "square" in sp and "root" not in sp:
                z = 1
                print("The answer is", nos[0] ** 2)
                speak("The answer is")
                speak(nos[0] ** 2)
            if "cube" in sp and "root" not in sp:
                z = 1
                print("The answer is", nos[0] **3)
                speak("The answer is")
                speak(nos[0] **3)
            if "to the power" in sp:
                z = 1
                print("The answer is",nos[0]**nos[1])
                speak("The answer is")
                speak(nos[0]**nos[1])
            if "square root" in sp:
                z = 1
                print("The answer is", nos[0] **0.5)
                speak("The answer is")
                speak(nos[0] **0.5)
            if "cube root" in sp:
                z = 1
                print("The answer is", nos[0] **(1/3))
                speak("The answer is")
                speak(nos[0] **(1/3))

            if "add" in sp or "plus" in sp or "+" in sp:
                z = 1
                print("The answer is",nos[0]+nos[1])
                speak("The answer is")
                speak(nos[0]+nos[1])
            if "subtract" in sp or "-" in sp or "minus" in sp:
                z = 1
                print("The answer is",nos[1]-nos[0])
                speak("The answer is")
                speak(nos[1]-nos[0])
            if "multiply"  in sp or "multiplied" in sp:
                z = 1
                print("The answer is",nos[0]*nos[1])
                speak("The answer is")
                speak(nos[0]*nos[1])
            if "divide"  in sp or  "divided" in sp:
                z = 1
                print("The answer is",nos[0]/nos[1])
                speak("The answer is")
                speak(nos[0]/nos[1])
            if "remainder" in sp:
                z = 1
                print("The answer is",nos[0]%nos[1])
                speak("The answer is")
                speak(nos[0]%nos[1])
            if "quotient" in sp or "%" in sp:
                z = 1
                print("The answer is",nos[1]//nos[0] * 100)
                speak("The answer is")
                speak(nos[1]//nos[0] * 100)
            if "roots" in sp or "quadratic" in sp and "equation" in sp:
                z = 1
                quad()
            if "sin" in sp:
                z = 1
                print("The answer is",math.sin(math.radians(nos[0])))
                speak("The answer is")
                speak(math.sin(math.radians(nos[0])))
            if "cos" in sp:
                z = 1
                print("The answer is",math.cos(math.radians(nos[0])))
                speak("The answer is")
                speak(math.cos(math.radians(nos[0])))
            if "tan" in sp:
                z = 1
                print("The answer is",math.tan(math.radians(nos[0])))
                speak("The answer is")
                speak(math.tan(math.radians(nos[0])))
            if "log" in sp and "base" not in sp:
                z = 1
                print("The answer is",math.log(nos[0]))
                speak("The answer is")
                speak(math.log(nos[0]))
            if "log" in sp and "base 10" in sp:
                z = 1
                print("The answer is",math.log10(nos[0]))
                speak("The answer is")
                speak(math.log10(nos[0]))
            if "circle" in sp and "perimeter" in sp and "diameter" not in sp:
                z = 1
                print("The answer is",nos[0]*2*3.14)
                speak("The answer is")
                speak(nos[0]*2*3.14)
            if "circle" in sp and "area" in sp and "diameter" not in sp:
                z = 1
                print("The answer is",3.14*(nos[0]**2))
                speak("The answer is")
                speak(3.14*(nos[0]**2))
            if "circle" in sp and "perimeter" in sp and "diameter" in sp:
                z = 1
                print("The answer is",nos[0]*3.14)
                speak("The answer is")
                speak(nos[0]*3.14)
            if "circle" in sp and "area" in sp and "diameter" in sp:
                z = 1
                print("The answer is",3.14*(nos[0]**2)/4)
                speak("The answer is")
                speak(3.14*(nos[0]**2)/4)
            if "prime" in sp:
                z = 1
                xp=nos[0]
                prime(xp)
            if "goodbye" in sp or "bye" in sp:
                print("See you later.")
                speak("See you later.")
                loading("Loading Jadoo! Dhoop!")
                break
            if "thanks" in sp or "thank you" in sp:
                print("That's what I'm here for.")
                speak("That's what I'm here for.")
                loading("Loading Jadoo! Dhoop!")
                break
            if "see you later" in sp:
                print("Nice helping you")
                speak("Nice helping you")
                loading("Loading Jadoo! Dhoop!")
                break
            if "help" in sp or "can you do" in sp:
                z = 1
                print("Here's a list of things I can help you with:")
                speak("Here's a list of things I can help you with:")
                print(" 1. I can do basic arithmetic such as Addition, Multiplication")
                speak(" 1. I can do basic arithmetic such as Addition, Multiplication")
                print(" 2. I can help you find area of circle")
                speak(" 2. I can help you find area of circle")
                print(" 3. I can help you find roots of a quadratic equation and plot a graph too!")
                speak(" 3. I can help you find roots of a quadratic equation and plot a graph too!")
            if z==0:
                print("Sorry didn't Catch That.")
                speak("Sorry didn't Catch That.")
        except IndexError:
            print('\033[1m'+"Bot:"+'\033[0m',"Please try again")
            speak("Please try again")
        except sr.UnknownValueError:
            print('\033[1m'+"Bot:"+'\033[0m',"Sorry didn't Catch That. ")
            speak("Sorry didn't Catch That. ")
        except sr.RequestError as e:
            print('\033[1m'+"Bot:"+'\033[0m',"Could not request nosults; {0}".format(e))
            speak("Could not request nosults {0}".format(e))


#function to check if the number is prime or not
def prime(x):
    y=""
    for i in range (2,x):
        if x%i==0:
            y="np"
            break
        else:
            y="p"
    if x==2:
        print("The answer is",",the number is a prime number")
        speak("The number is a prime number")
    if y=="np":
        print("The answer is",",the number is a NOT prime number")
        speak("The number is a NOT prime number")
    if y=="p":
        print("The answer is",",the number is a prime number")
        speak("The number is a prime number")


#Function to find the roots of a quadratic equation
def quad():
    try:
        def graph():
            e = []
            f = []
            for q in range(-50, 50, 1):
                p = a*(q**2) + b*q + c
                e.append(q)
                f.append(p)

            fig = plot.figure()
            axes = fig.add_subplot(111)
            axes.plot(e, f)
            plot.show()

        vi = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                print("Coefficient of X^2")
                speak("Coefficient of X^2")
                audio = vi.listen(source)
                a=eval(vi.recognize_google(audio))
                print(a):
            except:
                print("Coefficient of X^2")
                speak("Coefficient of X^2")
                audio = vi.listen(source)
                a=eval(vi.recognize_google(audio))
                print(a):
        with sr.Microphone() as source:
            try:
                print("Coefficient of X")
                speak("Coefficient of X")
                audio = vi.listen(source)
                b = eval(vi.recognize_google(audio))
                print(b)
            except:
                print("Coefficient of X")
                speak("Coefficient of X")
                audio = vi.listen(source)
                b = eval(vi.recognize_google(audio))
                print(b)
        with sr.Microphone() as source:
            try:
                print("Constant")
                speak("Constant")
                audio = vi.listen(source)
                c=eval(vi.recognize_google(audio))
                print(c)
            except:
                print("Constant")
                speak("Constant")
                audio = vi.listen(source)
                c=eval(vi.recognize_google(audio))
                print(c)

        graph()

        d=(math.sqrt(b**2-4*a*c))
        x=((d-b)/(2*a))
        y=((-b-d)/(2*a))
        print("Roots of",a,"X^2+","(",b,")X","+(",c,")",sep="",)
        speak("Roots of",a,"X^2+","(",b,")X","+(",c,")",sep="",)
        print("are",x,y)
        speak("are")
        speak(x)
        speak(y)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request nosults; {0}".format(e))
    except ValueError:
        print("Discriminant less than zero, Complex roots exist")


#funtion to speak a string
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Greeting function(Runs immediately on launch)
def onstartup():
    result = pyfiglet.figlet_format("JADOO" )
    print("\n")
    print(result)
    
    result = pyfiglet.figlet_format("Voice Assistant", font = "digital" )
    print(result)
    print("")


    print("\n")

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
        print("")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
        print("")   
    else:
        print("Good Evening!")
        speak("Good Evening!")
        print("")

    print("I am Jadoo- The voice Assistant!")
    speak("I am Jadoo- The voice Assistant!")
    print("")
    print("Developed by Ankit Gautam, Kartikey Dhaka and Himanshu Sachdeva")
    speak("Developed by Ankit Gautam, Kartikey Dhaka and Himanshu Sachdeva")
    print("")  
    print("What can I do for you?")
    speak("What can I do for you? ")       
    print("")


#Converts speech to text and generates the query
def returnCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("")
        print("👂 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("")
    try:
        print("")
        print("👀 Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        print("")
    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    onstartup()
    while True:
        query = returnCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'open geeks for geeks' in query:
            webbrowser.open("www.geeksforgeeks.org")   
        elif 'open music' in query:
            webbrowser.open("music.youtube.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The current time is {strTime}")    
            speak(f"The current time is {strTime}")
        elif 'code' in query:
            codePath = "C:\\Users\\Ankit Gautam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'coding' in query:
            codePath = "C:\\Users\\Ankit Gautam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'online classes' in query:
            sp.call("Zoom.exe")
        elif 'whatsapp' in query:
            sp.call("WhatsApp.exe")
        elif 'calculator' in query:
            sp.call("calc.exe")
        elif 'notepad' in query:
            sp.call("notepad.exe")
        # elif 'amazon music' or 'amazonmusic' in query:
        #     sp.call("Amazon Music.exe")
        elif 'open' in query:  
            webbrowser.open('www.'+query[5::]+'.com')
        elif 'spotify' in query:
            sp.call("Spotify.exe")
        elif 'play' in query:
            pywhatkit.playonyt(query[5::])
        elif 'baja do' in query:
            pywhatkit.playonyt(query[0:-8:])
        elif 'search' in query:
            webbrowser.open(query[7::])
        elif "weather" in query:
            city = query[19::]
            url = 'https://wttr.in/{}'.format(city)
            res = requests.get(url)
            print(res.text)
        elif "math" or "maths" or "mathbot" in query:
            mathbot()