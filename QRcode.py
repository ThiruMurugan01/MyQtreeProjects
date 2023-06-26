import qrcode

def generate_qr_code_from_text(text, output_path):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(output_path)

text = "Hey, there!"
output_path = "text_qr_code.png"
generate_qr_code_from_text(text, output_path)