from PIL import Image
import pytesseract
import os

image_path = os.path.join(os.path.dirname(__file__), '한글이미지.png')
image = Image.open(image_path)
text = pytesseract.image_to_string(image, lang='kor+eng')

print(text)

with open(os.path.join(os.path.dirname(__file__), '한글변환.txt'), 'w', encoding='utf-8') as f:
    f.write(text)
