import qrcode
import os

def generate_qr_code(data, file_path, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generate a QR code image and save it to a file.

    Args:
        data (str): The data to be encoded in the QR code.
        file_path (str): The file path to save the QR code image.
        error_correction (int): The error correction level.
        box_size (int): The size of each box in the QR code.
        border (int): The width of the border.
        fill_color (str): The color of the QR code squares.
        back_color (str): The background color of the QR code.

    Returns:
        None
    """
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )

    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image to a file
    img.save(file_path)

    print(f"QR code saved to {os.path.abspath(file_path)}")

# Data to be encoded in the QR code
data = "https://github.com/varsha2132"

# File path to save the QR code image
file_path = "qrcode.png"

# Additional features:
error_correction_level = qrcode.constants.ERROR_CORRECT_L
custom_box_size = 10
custom_border = 4
custom_fill_color = "black"
custom_back_color = "white"

# Generate and save the QR code with additional features
generate_qr_code(data, file_path, error_correction_level, custom_box_size, custom_border, custom_fill_color, custom_back_color)
