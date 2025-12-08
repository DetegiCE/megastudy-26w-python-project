import pytesseract

languages = pytesseract.get_languages(config='')
print(languages)
