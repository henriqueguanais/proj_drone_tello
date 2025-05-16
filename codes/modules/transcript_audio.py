import sounddevice as sd
import numpy as np
from vosk import Model, KaldiRecognizer
import json
import queue
import time

# Configurações
model_path = "models/vosk-model-pt-fb-v0.1.1-20220516_2113"
sample_rate = 16000
duration = 3  # Duração da gravação em segundos

# Inicializa o modelo Vosk
model = Model(model_path)
recognizer = KaldiRecognizer(model, sample_rate)

# Fila para armazenar o áudio
audio_queue = queue.Queue()

def _callback(indata, frames, time, status):
    """Função chamada a cada bloco de áudio gravado."""
    audio_queue.put(indata.copy())

def convert_audio_to_text() -> str:
    """
    Captura áudio do microfone e converte para texto usando Vosk.
    
    Return:
        str: Texto transcrito do áudio.
    """
    # Gravação do áudio
    print("Gravando... (3 segundos)")
    with sd.InputStream(callback=_callback, dtype=np.int16, channels=1, samplerate=sample_rate):
        start_time = time.time()
        end_time = start_time + duration
        audio_buffer = []
        
        while time.time() < end_time:
            remaining = end_time - time.time()
            try:
                data = audio_queue.get(timeout=remaining)
                audio_buffer.append(data)
            except queue.Empty:
                break
    
    # Processa o áudio capturado
    if audio_buffer:
        full_data = np.concatenate(audio_buffer, axis=0)
        if recognizer.AcceptWaveform(full_data.tobytes()):
            result = json.loads(recognizer.Result())
        else:
            result = json.loads(recognizer.FinalResult())
        
        print("Texto transcrito:", result.get("text", ""))
        return result.get("text", "")
    else:
        print("Nenhum áudio foi capturado.")
        return ""

if __name__ == "__main__":
    # Executa a função de conversão
    text = convert_audio_to_text()
    print("Texto final:", text)
    print(type(text))