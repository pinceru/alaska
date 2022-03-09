import pyaudio
import speech_recognition as sr
import pyttsx3
import json
from vosk import Model, KaldiRecognizer

def captura():
    model = Model('/home/welington/Downloads/vosk-model-small-pt-0.3')
    recognizer = KaldiRecognizer(model, 16000)
    cap = pyaudio.PyAudio()
    stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            audio = recognizer.Result()
            jsonparsed = json.loads(audio);
            audio = jsonparsed['text']
            print(audio)
            if audio == "fim":
                break

def captura_audio():
    #Criando recnhecedor de fala
    r = sr.Recognizer()

    #Abrindo o microfone
    with sr.Microphone() as aberto:
        while True:
            audio = r.listen(aberto) #Definindo o microfone como fonte de audio
            print(r.recognize_google(audio, language='pt'))

def test():
    engine = pyttsx3.init()
    engine.setProperty("voice", "brazil") #Definindo o idioma da voz
    engine.setProperty("rate", 180) #Definindo a velocidade da voz
    engine.setProperty("volume", 1.) #Definindo o volume da voz
    engine.say("Oi, eu sou a Alaska")
    engine.runAndWait()

def teste_interacao():
    model = Model('/home/welington/Downloads/vosk-model-small-pt-0.3')
    recognizer = KaldiRecognizer(model, 16000)
    cap = pyaudio.PyAudio()
    stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    engine = pyttsx3.init()
    engine.setProperty("voice", "brazil")
    engine.setProperty("rate", 140)
    engine.setProperty("volume", 1.5)
    with sr.Microphone() as aberto:
        engine.say("quem é?")
        engine.runAndWait()
        while True:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                audio = recognizer.Result()
                jsonparsed = json.loads(audio);
                audio = jsonparsed['text']
                print(audio)
                if audio == ('a marta'):
                    engine.say("oi, martha, fala uma banda daora pra eu ouvir")
                    engine.runAndWait()
                    break
                else:
                    engine.say("Não entendi o que você disse")
                    engine.runAndWait()
                    break

if __name__ == "__main__":
    teste_interacao()