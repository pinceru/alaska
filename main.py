import speech_recognition as sr

def captura_audio():
    #Criando recnhecedor de fala
    r = sr.Recognizer()

    #Abrindo o microfone
    with sr.Microphone() as aberto:
        while True:
            audio = r.listen(aberto) #Definindo o microfone como fonte de audio
            print(r.recognize_google(audio, language='pt'))

if __name__ == "__main__":
    captura_audio()