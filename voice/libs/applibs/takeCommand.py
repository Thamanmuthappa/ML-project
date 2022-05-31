import speech_recognition as sr
from libs.applibs.speak import speak

def takeCommand():
    '''
    Define a function to take command from the user   
    '''
    robot_ear = sr.Recognizer() 
    with sr.Microphone() as mic:
        #print("voice: Listening...")
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio, language = "en-in").lower() 
        #print("          You: " + you)
    except:
        you = ""
        speak("Pardon, please say again")
        return "None" # do not return
    return you
