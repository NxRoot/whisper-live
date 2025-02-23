from multiprocessing import freeze_support, set_start_method
from faster_whisper import WhisperModel
import speech_recognition as sr
import numpy as np
import tempfile
import wave
import sys
import os

isProd = getattr(sys, 'frozen', False)

def get_model_path():
    """Get the correct path to the model directory whether running as script or frozen exe"""
    if isProd:
        # Running in PyInstaller bundle
        return os.path.join(sys._MEIPASS, "model")
    else:
        # Running as normal Python script
        return "./model"

# You can choose compute type based on your hardware. Options: "int8", "float16", or "float32"
model = WhisperModel(get_model_path(), device="cpu", compute_type="int8")

def hprint(text):
    """
    Conditional print
    """
    if "--verbose" in sys.argv or not isProd:
        print(text, flush=True)


def save_audio_to_wav(audio_data, sample_rate):
    """
    Save audio data to a temporary WAV file
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
        with wave.open(temp_audio.name, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(audio_data)
        return temp_audio.name


def transcribe_audio(audio_path):
    """
    Transcribe audio using the loaded model
    """
    segments, _ = model.transcribe(
        audio_path,
        language="en",  # Force English language
        task="transcribe",  # Specifically for transcription
        beam_size=5  # Increase beam size for better accuracy
    )

    # Print the transcribed text
    for segment in segments:
        res = segment.text.strip()
        if (len(res) > 1):
            print(res, flush=True)


def listen_and_transcribe():
    """
    Continuously listen to microphone input and transcribe
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        hprint("# --> Listening... Speak to the microphone (Ctrl+C to stop)")

        temp_path = None  
        while True:
            try:
                # Listen for audio input
                audio = r.listen(source, phrase_time_limit=None)

                # Convert audio to wav file
                audio_data = np.frombuffer(audio.get_raw_data(), dtype=np.int8)
                temp_path = save_audio_to_wav(audio_data, audio.sample_rate)

                # Transcribe the audio
                transcribe_audio(temp_path)

                # Clean up temporary file
                os.unlink(temp_path)

            except KeyboardInterrupt:
                hprint("# --> Stopping transcription...")
                if temp_path != None and os.path.exists(temp_path): os.unlink(temp_path)
                break
            except Exception as e:
                hprint(f"# --> Error occurred: {str(e)}")
                if temp_path != None and os.path.exists(temp_path): os.unlink(temp_path)
                break


if __name__ == "__main__":
    hprint("# --> Starting Whisper Live...")
    freeze_support()
    set_start_method('spawn')
    listen_and_transcribe()
    os._exit(0)
