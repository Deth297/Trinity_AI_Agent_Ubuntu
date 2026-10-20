import webbrowser
from playsound3 import playsound
import urllib
import random
import tkinter as tk
from pathlib import Path

from speech_to_text import record_text
import subprocess 
import os 
TRINITY_DIR = Path(__file__).resolve().parent.parent
command = False
command_exicuted = False
global_sound_enabled = True


def play_sound(sound_file):
    if global_sound_enabled:
        playsound(sound_file)

def output_text(text):
    f = open(TRINITY_DIR / "Scripts" / "output.txt", "a")
    f.write(text + "\n")
    f.close()
    return

def VoiceCommands():
    global command_exicuted
    global command
    while True:
        text = record_text()
        if text:
            text = text.lower()
            output_text(text)
            command = False
        

            #commands List

            #command 1
            if text == "hello":
                play_sound(TRINITY_DIR / "AI_Voice_Responces" / "hello-hope-your-doing-well.mp3")

            #command 2
            if text == "trinity exit":
                play_sound(TRINITY_DIR / "AI_Voice_Responces" / "ok[pause]-see-you-one-the-other-side.mp3.mp3")

            
            #command 3
            if text == "trinity open brave" or text == "trinity open browser":
                command = True
                subprocess.Popen(["brave"])

            #command 4
            if text == "trinity open youtube":
                command = True 
                subprocess.Popen(["brave","https://www.YouTube.com"])

            #command 5
            if text == "trinity open steam":
                command = True
                subprocess.Popen(["brave","https://store.steampowered.com/"])

            #command 6
            if text == "trinity open discord":
                command = True
                subprocess.Popen(["discord"])

            #command 7
            if text == "trinity open spotify":
                command = True
                subprocess.Popen(["spotify"])

            #command 8
            if text == "trinity open github":
                command = True
                subprocess.Popen(["brave","https://www.github.com"])

            #command 9
            if text == "trinity open reddit":
                command = True
                subprocess.Popen(["brave","https://www.reddit.com"])

            #command 10
            if text == "trinity flip a coin":
                command = True
                result = random.choice(["Heads", "Tails"])
                print(f"The coin landed on {result}")

            #command 11
            if text == "trinity give me a number":
                command = True
                result = random.randint(1, 100)
                print(f"The random number is {result}")

            #command 12
            if text.startswith("trinity look up"):
                command = True
                query = text[len("trinity look up"):].strip()
                webbrowser.open(f"https://search.brave.com/search?q={urllib.parse.quote_plus(query)}")

            

            if command == True:  
                command_exicuted = True
                
                Responce = random.randint(1, 4)
                
                if Responce == 1:
                    play_sound(TRINITY_DIR / "AI_Voice_Responces" / "as-you-wish.mp3")
                
                if Responce == 2:
                    play_sound(TRINITY_DIR / "AI_Voice_Responces" / "process-completed.mp3")
                
                if Responce == 3:
                    play_sound(TRINITY_DIR / "AI_Voice_Responces" / "sure.mp3")
                
                if Responce == 4:
                   play_sound(TRINITY_DIR / "AI_Voice_Responces" / "whatever-you-say.mp3")


            


                
                
                
                

if __name__ == "__main__":
    VoiceCommands()
