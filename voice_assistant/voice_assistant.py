import speech_recognition as sr
import pyttsx3
import os

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def handle_command(command):
    """Handle commands based on the recognized text."""
    if 'open notepad' in command:
        os.system('notepad.exe')
        speak("Opening Notepad")
    elif 'play music' in command:
        os.system('start wmplayer')
        speak("Playing music")
    # Add more commands as needed


    """Main function to listen for commands and process them."""
    with sr.Microphone() as source:
        speak("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            handle_command(text.lower())
        except sr.UnknownValueError:
            speak("Sorry, I did not understand the audio.")
        except sr.RequestError:
            speak("Sorry, there was an error with the request.")

if __name__ == "__main__":
    main()
