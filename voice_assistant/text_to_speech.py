import speech_recognition as sr
import pyttsx3
import os

# Initialize components
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    with sr.Microphone() as source:
        speak("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            speak("You said: " + text)
        except sr.UnknownValueError:
            speak("Sorry, I did not understand the audio.")
        except sr.RequestError:
            speak("Sorry, there was an error with the request.")

if __name__ == "__main__":
    
