import pyttsx3 #pip install pyttsx3: for text data tp speech

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
    
while True:
    voice = int(input("Press 1 for male Voice\nPress 2 for female voice\n"))
    #speak(audio)
    getvoices(voice)
