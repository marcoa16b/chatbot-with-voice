import pygame
from gtts import gTTS
import os

class TextToSpeechModule:
  def __init__(self, lang="es", tld="es") -> None:
    self.lang = lang
    self.tld = tld
    self.filename = "tmp.mp3"

  def speak(self, text):
    pygame.init()
    tts = gTTS(text, lang=self.lang, tld=self.tld)
    tts.save(self.filename)
    pygame.mixer.init()
    pygame.mixer.music.load(self.filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    os.remove(self.filename)
    pygame.quit()

