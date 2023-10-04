
import os 
from dotenv import load_dotenv
import pyttsx3  
import speech_recognition as sr 
from bardapi import Bard
import requests
from dotenv import load_dotenv

load_dotenv()
bard_key = os.getenv('BARD_KEY')
os.environ['_BARD_API_KEY'] = bard_key
session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
# session.cookies.set("__Secure-1PSID", token) 

bard = Bard(session=session, timeout=30)

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

def max_sentence(text, max_length):
    # Split the text into sentences
    sentences = text.split('\n')
    
    # Filter sentences based on their length
    valid_sentences = [sentence.strip() for sentence in sentences if len(sentence.strip()) <= max_length]
    
    # Find the longest sentence among the valid ones
    if valid_sentences:
        longest_sentence = max(valid_sentences, key=len)
        return longest_sentence
    else:
        return None  # No valid sentences found

def API_Request(message):
    response = bard.get_answer(message)['content']
    #response = max_token(response, 30)
    #response = max_sentence(response, 2)
    message = response

    return message
messages = "Hi, Act like you are jarvis from ironman"

while(1):
    

    response = API_Request(messages)
    if response.find("*"):
        response = response.replace("*", "")
    x = max_sentence(response, 150)
    SpeechText(response)
    print(response)
    text = record_text()
    print(text)
    messages = text + "only give a very brief answer"
    if messages.find("shut up") != -1:
        break

