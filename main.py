import qrcode

def qr_code_generator(data, qr_image_name):

    try:
        qr = qrcode.QRCode(version=1,
                      error_correction=qrcode.constants.ERROR_CORRECT_L,
                      box_size=10,
                      border=4
                      )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save(qr_image_name)

        print(f"QR code generated and saved as {qr_image_name}")
    except Exception as e:
        print(f"{e} error occurred.")


if __name__ == "__main__":
    data = "https://github.com/adiver120"

    qr_image_name="generated_code.png"
    qr_code_generator(data, qr_image_name)









