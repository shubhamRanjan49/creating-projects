import os
import time
import openai
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv

def load_api_key():
    """Loads the OpenAI API key from the .env file."""
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("API key not found. Please check your .env file.")

def speak_text(text):
    """Converts text to speech."""
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in text-to-speech: {e}")

def record_audio():
    """Records audio and converts it to text."""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening...")
            audio = r.listen(source, timeout=10)
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
    except sr.WaitTimeoutError:
        print("Listening timed out.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except Exception as e:
        print(f"Unexpected error in speech recognition: {e}")

def send_to_chatgpt(messages, model="gpt-3.5-turbo"):
    """Sends messages to ChatGPT and returns the response."""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": message})
        return message
    except openai.error.RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
        time.sleep(60)
        return send_to_chatgpt(messages, model)
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return "An error occurred. Please try again later."

def main():
    """Main loop for the conversation."""
    load_api_key()
    messages = []
    while True:
        text = record_audio()
        if text:
            messages.append({"role": "user", "content": text})
            response = send_to_chatgpt(messages)
            speak_text(response)
            print("ChatGPT:", response)

if __name__ == "__main__":
    main()
