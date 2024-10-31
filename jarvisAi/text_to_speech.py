import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def record_text():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening...")
                audio = r.listen(source)
                text = r.recognize_google(audio)
                return text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Could not understand the audio")

def output_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    text = record_text()
    print("Recognized text:", text)
    output_text(text)
    
    
    print("wrote text")
