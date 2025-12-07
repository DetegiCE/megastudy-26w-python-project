from os import linesep
import googletrans
import asyncio

async def main():
    translator = googletrans.Translator()

    read_file_path = 'Ch09/영어파일.txt'
    write_file_path = 'Ch09/한글파일.txt'

    with open(read_file_path, 'r', encoding='utf-8') as f:
        readLines = f.readlines()

    for line in readLines:
        result1 = await translator.translate(line, dest='ko')
        print(result1.text)
        with open(write_file_path, 'a', encoding='utf-8') as f:
            f.write(result1.text + linesep)

asyncio.run(main())
