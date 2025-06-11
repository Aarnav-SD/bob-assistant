import queue
import sounddevice as sd
import vosk
import json
import threading

model = vosk.Model(lang="en-us")
q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    q.put(bytes(indata))


def listen_for_wake_word(wake_word="bob"):
    print("[Voice] Listening for wake word: 'Bob'...")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").lower()
                if wake_word in text:
                    print("[Voice] Wake word detected!")
                    return  # Exit when wake word is detected


def transcribe_command():
    print("[Voice] Listening for command...")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        transcript = ""
        timeout = 5  # seconds to pause to end capture
        silence_timer = 0

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    transcript += " " + text
                    silence_timer = 0
            else:
                silence_timer += 1

            if silence_timer > timeout:
                break

        print(f"[Voice] Final transcript: {transcript.strip()}")
        return transcript.strip()


def listen_and_transcribe():
    listen_for_wake_word()
    return transcribe_command()
