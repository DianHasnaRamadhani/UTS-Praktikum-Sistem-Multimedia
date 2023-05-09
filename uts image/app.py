from flask import Flask, render_template, request 
import cv2
import PIL
from PIL import Image
from tkinter.filedialog import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/after', methods=['GET', 'POST'])
def after():
    img = request.files['file1']

    img.save('static/file.jpg')

    image = cv2.imread('static/file.jpg', 0)
    invert = cv2.bitwise_not(image)
    blur = cv2.GaussianBlur(invert, (21,21),0)
    inverteblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(image, inverteblur, scale=256.0)
    sketsa = cv2.imwrite("sketsa.png", sketch)

    path = "sketsa.png"
    gambar = PIL.Image.open(path)
    height, width = gambar.size
    imgCompres = gambar.resize((height, width), PIL.Image.ANTIALIAS)
    save = imgCompres.save('static/compress.png')


    return render_template('after.html')

if __name__ == "__main__":
    app.run(debug=True)