from os import linesep
import googletrans
import asyncio

async def main():
    translator = googletrans.Translator()

    read_file_path = 'Ch09/영어파일.txt'

    with open(read_file_path, 'r', encoding='utf-8') as f:
        readLines = f.readlines()

    for line in readLines:
        result1 = await translator.translate(line, dest='ko')
        print(result1.text)

asyncio.run(main())
