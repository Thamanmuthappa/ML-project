from libs.applibs.jokes import *
from libs.applibs.sendEmail import *
from libs.applibs.sound import *
from libs.applibs.speak import *
from libs.applibs.takeCommand import *
from libs.applibs.time import *

import webbrowser
import time
# import wikipedia

def robot():
    openSound()
    print("      Loading voice assistant...")

    while True:
        you = takeCommand().lower()
        if you == "":
            continue
        # say hello
        elif ("hello" in you) or ("hi " in you):
            wishMe()
        # what time is it?
        elif ("time" in you):
            get_time()
        # get date
        elif ("date" in you):
            get_date()
        #jokes
        elif ("joke" in you):
            get_joke()
        # play a song
        elif "play a song" in you:
            sing()
        elif "sing " in you:
            speak("I can't sing, but I can play a song. ")
            sing()
        elif " bored" in you:
            speak("Let me entertain you. I can tell you a joke or play a song")
        elif 'who are you' in you or 'what can you do' in you:
            speak('I am voice version 1 point O your personal assistant. I am programmed to minor tasks like'
                'opening youtube, google, gmail, facebook and youtube ,predict time,search wikipedia.' 
                'I also can play a song!')

        elif "who made you" in you or "who created you" in you or "who discovered you" in you:
            speak("I was built by Bhagya")
        # search on the Internet
        elif "search"  in you:
            you = you.replace("search", "")
            webbrowser.open_new_tab(you)
            time.sleep(1)
            break
        # search on Wikipedia
        # if ("wikipedia" in you) :
        #     speak('Searching Wikipedia...')
        #     you =you.replace("wikipedia", "")
        #     results = wikipedia.summary(you, sentences=3)
        #     speak("According to Wikipedia")
        #     speak(results)
        # open Youtube
        elif "open youtube" in you or ("listen to music" in you):
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(1)
            break
        # open Google
        elif "open google" in you:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(1)
            break
        # open Gmail
        elif "open gmail" in you:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(1)
            break
        # open Facebook
        elif "open facebook" in you:
            webbrowser.open_new_tab("https://www.facebook.com/")
            speak("Facebook open now")
            time.sleep(1)
            break
        # search some definitions
        elif "what is"  in you:
            webbrowser.open_new_tab(you)
            results = wikipedia.summary(you, sentences=1)
            speak(results)
            time.sleep(1)
            break
        # send an email
        elif "send an email" in you:
        
            speak("Who do you want to send the email to?")
            # get the receiver's information
            receiver = ''
            you = takeCommand().lower()
            while receiver == '':
                if ("quit" in you) or ("exit" in you): #exit send-email function
                    break
                elif "apple" in you:
                    receiver = "apple"
                    sendEmail(receiver)   
                elif "jenny" in you:
                    receiver = "jenny"
                    sendEmail(receiver)   
                elif "me" in you:
                    receiver = "me"
                    sendEmail(receiver)   
                elif you != "":
                    speak("Sorry, I haven't saved this person's email "
                        "Let you choose the other."
                            # "Let you help me by saying 'add email'."
                        " If you want to quit the process, please say 'quit' or say 'exit'")
                    # add email function - improve later
                    you = takeCommand().lower()
                    if ("quit" in you) or ("exit" in you): #exit send-email function
                        break                   
                
        # end the conversation
        elif ("bye" in you) or ("okay" in you) or ("thank" in you) or ("stop" in you):
            #speak("Good bye! I'm shutting down, see you later!")
            speak("Okay! Anytime you want to talk with me, press the micro button!")
            break