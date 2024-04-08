from gtts import gTTS

with open(file="randompost.txt", mode="r") as f:  
  mylist = [line.rstrip('\n') for line in f]
  print(mylist)
  newstr = ','.join(mylist)
  tts_post = gTTS(text=newstr, lang_check='en')

tts_post.write_to_fp('test.mp3')