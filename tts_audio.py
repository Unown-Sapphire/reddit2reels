from openai import * 
client  = OpenAI(
    api_key="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"
)

headers = {
    "Content-Type" : "text/plain",
    "Authorization": "Bearer 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"
}

audio_file= open("test.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcript)