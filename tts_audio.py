import whisper
from whisper.utils import get_writer
import torch
from TTS.api import TTS
from pydub.effects import speedup
from pydub import AudioSegment

device = "cuda" if torch.cuda.is_available() else "cpu"

from pydub import AudioSegment
import re

import os, shutil
folder = 'audios'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

# Function to split text into chunks
def split_text(text, max_length=250):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_length:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    for chunk in chunks:
        if chunk == ".":
            chunks.remove(chunk)
        
    return chunks

# Function to synthesize chunks into audio segments
def synthesize_text(text):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    chunks = split_text(text)
    n = 1
    for chunk in chunks:
        if n <= 9:
            tts.tts_to_file(chunk, speaker="Abrahan Mack", language="en", file_path=f"audios/line_0{n}.wav")
            n+=1
        else:
            tts.tts_to_file(chunk, speaker="Abrahan Mack", language="en", file_path=f"audios/line_{n}.wav")
            n+=1
def combine_audio():
    audiosegment_list = []
    combined_list = os.listdir(path="audios")
    for i in combined_list:
        audio = AudioSegment.from_wav(f"audios/{i}")
        audiosegment_list.append(audio)
    full_audio = sum(audiosegment_list)
    full_audio.export("output.wav", format="mp3")

def speedup_audio():
    sound = AudioSegment.from_mp3("output.wav")
    sound = speedup(seg=sound, playback_speed=1.2)
    sound.export("audios/spedup.mp3", format="mp3")  

with open ("randompost.txt", encoding='utf-8') as randomposts:
    posts = randomposts.read()

audio_segments = synthesize_text(text=posts)
print("---> Synthesized speech...")
combine_audio()
print("---> Combined Audio...")
speedup_audio()
print('---> Sped up audio...')

print("Process over...")

word_options = {
    "max_line_count": 1,
    "max_line_width": 20
}

model = whisper.load_model('base')
audio = whisper.load_audio("audios/spedup.mp3")
result = whisper.transcribe(model, audio, word_timestamps=True)

# Save as an SRT file
srt_writer = get_writer("srt", ".")
srt_writer(result, "audios/spedup.mp3", {"max_words_per_line":3})

print("---> Finished writing spedup.srt")