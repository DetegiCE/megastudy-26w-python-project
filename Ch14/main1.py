from PIL import Image
import pytesseract
import os

image_path = os.path.join(os.path.dirname(__file__), '한글이미지.png')
image = Image.open(image_path)
text = pytesseract.image_to_string(image, lang='kor')

print(text)