import torch
from TTS.api import TTS
import os

device = "cuda" if torch.cuda.is_available() else "cpu"

from pydub import AudioSegment
import re

# Function to split text into chunks
def split_text(text, max_length=500):
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
    
    return chunks

# Function to synthesize chunks into audio segments
def synthesize_text(text):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    chunks = split_text(text)
    n = 1
    for chunk in chunks:
        audio_segments = tts.tts_to_file(chunk, speaker="Ana Florence", language="en", file_path=f"audios/line_{n}.wav")
        n+=1
def combine_audio(audio: str):
    combined = os.listdir(path="audios")
    

with open ("randompost.txt", encoding='utf-8') as randomposts:
    posts = randomposts.read()

text = posts
audio_segments = synthesize_text(text)