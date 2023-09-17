import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 
openai.api_base = os.getenv("OPENAI_API_BASE_URL")

class SpeechRecognitionModule:
    def __init__(self, lang="es"):
        self.lang = lang
        self.recognizer = sr.Recognizer()

    def recognize(self):
        with sr.Microphone() as source:
          print("Speack Anything : ")
          audio = self.recognizer.listen(source)
          try:
              text = self.recognizer.recognize_google(audio, language=self.lang)
              return text
          except Exception as exc:
              return f"Exception occurred: {exc}"

class TextToSpeechModule:
    def __init__(self, voice=0, volume=1, rate=125) -> None:
        self.voice = voice
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

        voices = self.engine.getProperty("voices")
        
        self.engine.setProperty("voice", voices[voice].id)

    def talk(self, text):
        """
        Function to convert text to speech.
        """
        self.engine.say(text)
        self.engine.runAndWait()
    
recognition = SpeechRecognitionModule()
speaker = TextToSpeechModule()

def getResponse(messages):
    res = openai.ChatCompletion.create(
        model="accounts/fireworks/models/llama-v2-7b-chat",
        messages=messages
    )
    return res.choices[0].message
    

def main():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    while True: 
        text = recognition.recognize()
        if text:
            print("pensando...")
            input=f"Responde en español y de forma consisa y breve. {text}"
            content = {
                "role": "user",
                "content": input
            }
            messages.append(content)
            response = getResponse(messages)
            speaker.talk(response.content)
            messages.append(response)
        else:
            speaker.talk("Lo siento, no te he entendido.")

main()