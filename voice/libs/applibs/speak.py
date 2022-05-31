import pyttsx3

# use Sapi5 of Microsoft for text-to-speech 
robot_mouth = pyttsx3.init('sapi5') 
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice','voices[1].id')
                                    # 0: man's voice
                                    # 1: woman's voice

def speak(text):
    '''
    Text-to-speech function
    '''
    robot_mouth.say(text)
    #print("voice: " + text)
    robot_mouth.runAndWait()