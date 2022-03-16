import pyttsx3
import pyaudio
from vosk import Model, KaldiRecognizer

def voice():
    engine = pyttsx3.init()
    engine.setProperty("voice", "brazil_rp+f4")
    engine.setProperty("rate", 100)
    engine.setProperty("volume", 1.5)
    return engine

def url():
    model = Model('/home/welington/Downloads/vosk-model-small-pt-0.3')
    return model

def stream():
    cap = pyaudio.PyAudio()
    return cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)