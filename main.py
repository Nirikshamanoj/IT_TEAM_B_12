import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
# converts the text to speech
import pyttsx3

# translates into the mentioned language
from googletrans import Translator

# read image
from flask import Flask, render_template, request
from flask import session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

def image_to_text(file_name):
    path_1 = r"C:\Users\REVA\PycharmProjects\text\image" + file_name
    text_org = ""
    image_path = path_1

    img = cv2.imread(image_path)
    reader = easyocr.Reader(['en'], gpu=False)
    text_ = reader.readtext(img)

    threshold = 0.25
    for t_, t in enumerate(text_):
        bbox, text, score = t
        if score > threshold:
            text_org = text_org + " " + text

    return text_org

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        file_name = f.filename
        f.save(r"C:\Users\REVA\PycharmProjects\text\image" + str(file_name))
        text = image_to_text(file_name)
        session['recognized_text'] = text  # Store the recognized text in the session
        recognized_text = session.get('recognized_text')  # Fetch recognized text from the session
        return render_template("1.html", name=recognized_text)


if __name__ == '__main__':
    app.run()




if __name__ == '__main__':
    app.run()
