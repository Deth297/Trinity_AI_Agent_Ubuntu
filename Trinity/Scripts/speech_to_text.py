from logging import root
from tkinter import Image

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
r.dynamic_energy_threshold = True
r.energy_threshold = 300
startup = False
processing = False

def record_text():
    global startup, processing
    while(1):
        try:
            # Use the headset microphone
            with sr.Microphone() as source2:

                print("Listening... Speak now!")
                startup = True
                    
                
                # listen for the user's input
                audio2 = r.listen(source2)
                startup = False

                print("proccessing...")
                processing = True

                try:
                    # Using google to recognize audio
                    my_text = r.recognize_google(audio2)
                finally:
                    processing = False

                return my_text

        except sr.RequestError as e:
            print("ERROR: Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("ERROR: Unknown error occurred")
            continue

