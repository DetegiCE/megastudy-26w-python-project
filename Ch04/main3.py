from gtts import gTTS
from pygame import mixer
import os

# 경로는 .py 파일의 실행 경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '나의텍스트.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    read_file = file.read()

tts = gTTS(text=read_file, lang='ko')
tts.save("mytext.mp3")

mixer.init()
mixer.music.load("mytext.mp3")
mixer.music.play()
while mixer.music.get_busy():
    pass
mixer.quit()
