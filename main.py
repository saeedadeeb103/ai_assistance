import openai
import os 
from dotenv import load_dotenv
import pyttsx3  
import speech_recognition as sr 
from bardapi import Bard

os.environ['_BARD_API_KEY'] = 'bwjtNKZxQ4zwPDGGN7h1HupgzbsqK-aPWpOJM2HtIjujcfQayWLWMkoQq5IC0euAhFJbsw.'


def SpeechText(voice):

    engine = pyttsx3.init()
    engine.say(voice)
    engine.runAndWait()

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                
                print("I'm Listening")
                audio = r.listen(source)

                MyText = r.recognize_google(audio)

                return MyText
            
        except sr.RequestError as e:
            print("Could not Request Results; {0}".format(e))
        
        except sr.UnknownValueError:
            print("Unknown Error Occurred")


def API_Request(messages):
    response = Bard().get_answer(messages[0]['content'])['content']
    message = response
    messages.append(response)

    return message
messages = [{"content": "Act like you are jarvis from ironman "}]

while(1):
    text = record_text()
    messages.append({"content": text})

    response = API_Request(messages)
    SpeechText(response)

    print(response)


