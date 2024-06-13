from flask import Flask, request, render_template, send_file
from PIL import Image
from cryptography.fernet import Fernet
import os
import io

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
KEY_PATH = 'secret.key'

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, 'wb') as key_file:
        key_file.write(key)
    return key

# Function to load a key
def load_key():
    return open(KEY_PATH, 'rb').read()

# Function to encrypt a message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)
    return decrypted_message.decode()

# Function to encode an image with a message
def encode_image(image_path, message, key):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    encrypted_message = encrypt_message(message, key)
    binary_message = ''.join([format(byte, '08b') for byte in encrypted_message]) + '1111111111111110'

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for n in range(3):  # Loop through RGB
                if index < len(binary_message):
                    pixel[n] = pixel[n] & ~1 | int(binary_message[index])
                    index += 1
            encoded.putpixel((col, row), tuple(pixel))

            if index >= len(binary_message):
                break
        if index >= len(binary_message):
            break

    encoded_io = io.BytesIO()
    encoded.save(encoded_io, format='PNG')
    encoded_io.seek(0)
    return encoded_io

# Function to decode a message from an image
def decode_image(image_path, key):
    img = Image.open(image_path)
    binary_message = ''
    width, height = img.size

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for n in range(3):  # Loop through RGB
                binary_message += str(pixel[n] & 1)

    message_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message_bytes = [int(byte, 2) for byte in message_bytes]

    end_idx = 0
    for i in range(len(message_bytes)):
        if message_bytes[i:i+2] == [255, 254]:
            end_idx = i
            break

    encrypted_message = bytes(message_bytes[:end_idx])
    decrypted_message = decrypt_message(encrypted_message, key)
    return decrypted_message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    if 'image' not in request.files or 'message' not in request.form:
        return "No image or message provided!", 400
    
    image = request.files['image']
    message = request.form['message']
    
    if not image or image.filename == '':
        return "No selected file", 400

    key = load_key()
    encoded_image = encode_image(image, message, key)
    
    return send_file(encoded_image, mimetype='image/png', as_attachment=True, attachment_filename='encoded_image.png')

@app.route('/decode', methods=['POST'])
def decode():
    if 'image' not in request.files:
        return "No image provided!", 400
    
    image = request.files['image']
    
    if not image or image.filename == '':
        return "No selected file", 400

    key = load_key()
    decoded_message = decode_image(image, key)
    
    return decoded_message

if __name__ == '__main__':
    # Generate key if it doesn't exist
    if not os.path.exists(KEY_PATH):
        generate_key()
    
    app.run(debug=True)
