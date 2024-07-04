from flask import Flask, request, render_template, send_from_directory
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extract_palette(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Resize for faster processing
    image = np.array(image)
    image = image.reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(image)
    palette = kmeans.cluster_centers_
    return palette.astype(int)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            palette = extract_palette(file_path)
            palette_hex = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in palette]
            return render_template('index.html', palette=palette_hex, image_url=file_path)
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
