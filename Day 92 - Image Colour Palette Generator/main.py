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

        return render_template('index.html', colors_list=dominant_colors, image=filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


#TODO
    # analysis - https://colab.research.google.com/drive/1loupRmuDJGitzdvMcTB7o7Etim_-bjdQ#scrollTo=Fg75QSPht7bK
    # transition after posting an image - title card goes on top, an analysis card on bottom
    # analysis card - picture on the left, top 10 colors on the right with the HEX code inside of them and their percentages

# reference: https://www.coolphptools.com/color_extract#demo
