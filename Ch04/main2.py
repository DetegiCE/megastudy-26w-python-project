from gtts import gTTS
from pygame import mixer
import os

# 경로는 .py 파일의 실행 경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요 저는 메가스터디에서 코딩을 배우고 있습니다."

tts = gTTS(text=text, lang='ko')
tts.save("greeting.mp3")

mixer.init()
mixer.music.load("greeting.mp3")
mixer.music.play()
while mixer.music.get_busy():
    pass
mixer.quit()
