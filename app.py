from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import cv2
import numpy as np

app = Flask(__name__)

def read_image(file_path):
    img = cv2.imread(file_path)
    return img

def edge_detection(img, line_wdt, blur):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayBlur = cv2.medianBlur(gray, blur)
    edges = cv2.adaptiveThreshold(grayBlur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_wdt, blur)
    return edges

def color_quantisation(img, k):
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        img = read_image(file_path)
        line_wdt = 9
        blur_value = 7
        total_colors = 6

        edge_img = edge_detection(img, line_wdt, blur_value)
        img = color_quantisation(img, total_colors)
        blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200, sigmaSpace=200)
        cartoon = cv2.bitwise_and(blurred, blurred, mask=edge_img)

        cartoon_path = os.path.join('static', 'cartoon.jpg')
        cv2.imwrite(cartoon_path, cartoon)

        return render_template('index.html', cartoon_path=cartoon_path)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

@app.route('/static/<filename>')
def static_file(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)
