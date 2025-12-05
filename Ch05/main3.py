import qrcode

file_path = r'Ch05/qr코드모음.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    read_lines = file.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = 'Ch05/' + qr_data + '.png'
        qr_img.save(save_path)

