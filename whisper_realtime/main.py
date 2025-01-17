import whisper
import sounddevice as sd
import numpy as np
import pyttsx3
from transcricao.main import ask


# Carregar o modelo Whisper
model = whisper.load_model("base")  # Escolha o modelo: "tiny", "base", etc.

def transcrever_audio():
    print("Iniciando transcrição em tempo real. Pressione Ctrl+C para parar.")
    samplerate = 16000  # Taxa de amostragem recomendada para Whisper
    duration = 5  # Duração do áudio capturado em segundos

    try:
        while True:
            print("\nGravando... Fale algo agora!")
            audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype="float32")
            sd.wait()  
            
            # Remove a dimensão extra
            audio = audio.flatten()

            print("Transcrevendo...")
            result = model.transcribe(audio, fp16=False, language="pt")
            
            transcricao = result["text"]
            print("Você disse:", transcricao)
            response = ask(transcricao)

            print(response)

            engine = pyttsx3.init()

            engine.setProperty("rate", 215)  
            engine.setProperty("volume", 0.9)  

            engine.say(response)
            engine.runAndWait()
    except KeyboardInterrupt:
        print("\nTranscrição encerrada. Obrigado por usar o sistema!")

if __name__ == "__main__":
    transcrever_audio()
