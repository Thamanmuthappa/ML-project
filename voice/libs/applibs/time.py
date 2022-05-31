from libs.applibs.speak import speak 
import datetime

def wishMe():
    '''
    Define a function to greet the user
    '''
    hour =  datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, good morning! What can I help you?")
    elif hour >= 12 and hour < 18:
        speak("Hello, good afternoon! What can I help you?")
    else:
        speak("Hello, good evening! What can I help you?")

def get_date():
    speak("Today is " + str(datetime.date.today()))
def get_time():
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak("It is " + strTime + " now")