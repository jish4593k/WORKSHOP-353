import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import torch
import threading
from tkinter import Tk, Entry, Button, Label

listener = sr.Recognizer()
player = pyttsx3.init()

# PyTorch transformations
transform = torch.nn.functional.interpolate
tensor_transform = torch.nn.functional.to_tensor

class VoiceBotGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Voice-Activated Bot")

        self.entry = Entry(self.root, width=40)
        self.entry.pack(pady=10)

        self.btn_listen = Button(self.root, text="Listen", command=self.listen_and_process)
        self.btn_listen.pack(pady=10)

        self.label_response = Label(self.root, text="")
        self.label_response.pack(pady=10)

    def listen_and_process(self):
        threading.Thread(target=self.run_voice_bot).start()

    def run_voice_bot(self):
        command = self.listen()
        if "sunny" in command:
            command = command.replace("sunny", "")
            if "what is" in command:
                command = command.replace("what is", "")
                info = wikipedia.summary(command, sentences=2)
                self.talk(info)
            elif "who is" in command:
                command = command.replace("who is", "")
                info = wikipedia.summary(command, sentences=2)
                self.talk(info)
            elif "play" in command:
                command = command.replace("play", "")
                pywhatkit.playonyt(command)
            else:
                self.talk("Sorry, I am unable to find what you're looking for")

    def listen(self):
        with sr.Microphone() as input_device:
            print("I am ready, Listening ....")
            voice_content = listener.listen(input_device)
            text_command = listener.recognize_google(voice_content)
            text_command = text_command.lower()
            print(text_command)

        return text_command

    def talk(self, text):
        self.label_response.config(text=text)
        player.say(text)
        player.runAndWait()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    voice_bot_gui = VoiceBotGUI()
    voice_bot_gui.run()
