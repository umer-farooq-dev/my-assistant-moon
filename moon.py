import pyttsx3 #pip install pyttsx3: for text data tp speech
import datetime
import speech_recognition as sr #pip install SpeechRecognition
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        
    speak("Hello this is moon")    

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")# I for Hour: M for minutes: S for seconds
    speak("The current Time is:")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The Current date is:")
    speak(month)
    speak(date)
    speak(year)
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour <18:
        speak("Good afternoon Sir!")
    elif hour >=18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir")
    
   
def wishme():
    speak("Welcome Back Sir:")
    time()
    date()
    greeting()
    speak("Moon at your Service , Please Tell me how can i help you")
    
      
# while True:
#     voice = int(input("Press 1 for male Voice\nPress 2 for female voice\n"))
#     #speak(audio)
#     getvoices(voice)

#time()
#wishme()

def takeCommandCMD():
    query = input("Please Tell me how can i help you: ")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizning.....")
        query = r.recognize_google(audio, language="en-NI")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again Please....")
        return "None"
    return query
        

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommandMic().lower()
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
    
    
