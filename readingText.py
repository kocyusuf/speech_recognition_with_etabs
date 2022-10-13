from gtts import gTTS
import os
from playsound import playsound
import time

myText = "Ne yapıyorsun?"
language = "tr"

output = gTTS(text=myText, lang=language, slow=False)
output.save("voice.mp3")
time.sleep(3)
playsound("voice.mp3")
#os.system("start voice.mp3")
