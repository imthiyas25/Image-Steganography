# 🖼️🔍 Image Steganography Project  

Welcome to the **Image Steganography** project! 🎉  
This project enables users to **hide and retrieve secret messages** within images using Python. It ensures **secure and invisible** data embedding, making it ideal for privacy-focused applications. 🕵️‍♂️🔓  

---

## 🚀 Introduction  

**Steganography** is the practice of concealing information within other non-secret data. In this project, we use **images** as the medium to embed and extract hidden messages seamlessly.  

This project leverages **Python** and the **Pillow** library to provide a simple yet powerful way to perform image steganography. 📷✨  

---

## 🌟 Features  

✅ **Encode Messages** – Hide a secret text within an image effortlessly.  
✅ **Decode Messages** – Retrieve the hidden message from an encoded image.  
✅ **User-Friendly Interface** – Simple and intuitive UI for easy interaction.  
✅ **Support for Multiple Image Formats** – Works with **PNG, JPG, and more**.  

---

## 🛠️ Technologies Used  

- **Python** 🐍 – Core language for the application  
- **Flask** 🌐 – Web framework for the frontend  
- **Pillow (PIL)** 📸 – Image processing library  

---

## 📥 Installation & Setup  

Follow these steps to set up and run the **Image Steganography** project on your local machine.  

### 🔧 Step 1: Clone the Repository  
```sh
git clone https://github.com/imthiyas25/Image-Steganography.git
cd Image-Steganography

###🔧 Step 2: Create a Virtual Environment (Recommended)
sh
Copy
Edit
# Create virtual environment
python -m venv venv  

# Activate it
# For Windows:
venv\Scripts\activate  
# For macOS/Linux:
source venv/bin/activate  
🔧 Step 3: Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
🔧 Step 4: Run the Application
sh
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:5000/

Upload an image and encode/decode secret messages easily.

📷 Example Usage
Encoding a Message
Upload an image (.png, .jpg, etc.).

Enter the secret message you want to hide.

Click "Encode" and download the new image with hidden data.

Decoding a Message
Upload the stego-image (image with hidden data).

Click "Decode" to extract the hidden message.
