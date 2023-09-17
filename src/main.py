"""
src/main.py: Main module to run the program.
"""

from dotenv import load_dotenv
from pyfiglet import Figlet
from speech import TextToSpeechModule

load_dotenv() # Load environment variables

def main():
  f = Figlet(font='epic')
  print(f.renderText('Aoi :D')) # Print ASCII art of the name of model

  speaker = TextToSpeechModule()
  speaker.speak("Hola, soy tu asistente personal, ahora estoy nuevamente en línea.")

  instructions = """
    Comandos principales:
      - h / H: Ayuda
      - s / S: Configuración
      - o / O: Opciones
      - q / Q: Apagar asistente
  """
  
  running = True

  while running:  
    print(instructions)

    option = input("Introduce un comando: ")
    match option:
      case "h" | "H":
        print("AYUDA")
      case "s" | "S":
        print("CONFIG")
      case "o" | "O":
        print("OPTIONS")
      case "q" | "Q":
        print("Bye Bye!!!")
        running = False
        

main()