import pyaudio
import speech_recognition as sr
import pyttsx3
import json
import config
from vosk import Model, KaldiRecognizer

def teste_interacao():
    model = config.url()
    recognizer = KaldiRecognizer(model, 16000)
    stream = config.stream()
    stream.start_stream()
    engine = config.voice()
    with sr.Microphone() as aberto:
        engine.say("Teste")
        engine.runAndWait()
        while True:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                audio = recognizer.Result()
                jsonparsed = json.loads(audio);
                audio = jsonparsed['text']
                print(audio)
                engine.say(audio)

if __name__ == "__main__":
    teste_interacao()