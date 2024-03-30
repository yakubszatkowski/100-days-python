from flask import Flask, render_template, request
from PIL import Image
from image_processing import dominant_colors_extraction
import os

UPLOAD_FOLDER = "./static/.cache"

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['picture-upload']
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
        filename = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
        pil_image = Image.open(filename)
        dominant_colors = dominant_colors_extraction(pil_image)
        filename = filename.replace(' ', '%20')

        print(dominant_colors)

        return render_template('index.html', colors_list=dominant_colors, image=filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


#TODO
    # remove images after usage

# reference: https://www.coolphptools.com/color_extract#demo
