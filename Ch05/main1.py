import qrcode

qr_data = 'megaunilab.com'
qr_img = qrcode.make(qr_data)

save_path = 'Ch05/' + qr_data + '.png'
qr_img.save(save_path)
