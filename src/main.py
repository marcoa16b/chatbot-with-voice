"""
src/main.py: Main module to run the program.
"""

from dotenv import load_dotenv
from pyfiglet import Figlet
from speech import TextToSpeechModule
from speech import SpeechToTextModule
import os

load_dotenv() # Load environment variables

speaker = TextToSpeechModule()

def listeningVoice():
  stt = SpeechToTextModule()
  while True:
    text = stt.recognize()
    if text:
      if "deja de escuchar" in text:
        break
      if "Exception occurred" in text:
        print(f"ERROR: {text}")
        break
      speaker.speak(f"Has dicho: {text}")
    else:
      speaker.speak("Lo siento. No te he entendido.")

def main():
  f = Figlet(font='epic')
  print(f.renderText('Aoi :D')) # Print ASCII art of the name of model

  #speaker = TextToSpeechModule()
  speaker.playSong("./assets/load-app.mp3")
  speaker.speak("Hola, soy tu asistente personal, ahora estoy nuevamente en línea.")

  instructions = """
  Comandos principales:
    - v / V: Escuchar voz
    - h / H: Ayuda
    - s / S: Configuración
    - q / Q: Apagar asistente
  """
  
  running = True

  while running:
    os.system("cls")
    print(instructions)

    option = input("Introduce un comando: ")
    match option:
      case "v" | "V":
        listeningVoice()
      case "h" | "H":
        print("AYUDA")
      case "s" | "S":
        print("CONFIG")
      case "o" | "O":
        print("OPTIONS")
      case "q" | "Q":
        print("Bye Bye!!!")
        running = False
      case _:
        print("Comando desconocido...")

main()