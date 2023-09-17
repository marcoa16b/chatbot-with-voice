import speech_recognition as sr

class SpeechToTextModule:
  def __init__(self, lang="es") -> None:
    self.lang = lang
    self.recognizer = sr.Recognizer()

  def recognize(self):
    with sr.Microphone() as source:
      print("Speack Anything : ")
      audio = self.recognizer.listen(source)
      try:
        text = self.recognizer.recognize_whisper(audio, language=self.lang)
        return text
      except Exception as exc:
        return f"Exception occurred: {exc}"