import pyttsx3 #pip install pyttsx3: for text data tp speech
import datetime
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
      
# while True:
#     voice = int(input("Press 1 for male Voice\nPress 2 for female voice\n"))
#     #speak(audio)
#     getvoices(voice)

#time()
date()
