from gtts import gTTS

text = "안녕하세요 저는 메가스터디에서 코딩을 배우고 있습니다."

tts = gTTS(text=text, lang='ko')
tts.save("Ch04/greeting.mp3")
