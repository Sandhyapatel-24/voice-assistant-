import pyttsx3
import speech_recognition as sr
from time import strftime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, the service is unavailable."

if __name__ == "__main__":
    speak("Hello, I am your voice assistant. How can I help you?")
    try:
        while True:
            command = listen().lower()
            print("You:", command)
            if "exit" in command or "bye" in command:
                speak("Goodbye!")
                break
            elif "hello" in command:
                speak("Hello! How are you?")
            elif "time" in command:
                speak("The time is " + strftime("%H:%M %p"))
            else:
                speak("I don't understand.")
    except KeyboardInterrupt:
        print("\nVoice Assistant Stopped.")
        speak("Goodbye!")
