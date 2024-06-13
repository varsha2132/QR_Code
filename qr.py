import qrcode

# Data to be encoded in the QR code
data = "https://github.com/varsha2132"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code, 1 is the smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the QR code
    border=4,  # width of the border (minimum is 4)
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")
