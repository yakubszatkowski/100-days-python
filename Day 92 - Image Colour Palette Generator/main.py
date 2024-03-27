from flask import Flask, render_template, request
from PIL import Image
from image_processing import dominant_colors_extraction
import os, tempfile

temp_dir = tempfile.TemporaryDirectory()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['picture-upload']
        image.save(os.path.join(temp_dir.name, image.filename))
        filename = os.path.join(temp_dir.name, image.filename)
        pil_image = Image.open(filename)
        dominant_colors = dominant_colors_extraction(pil_image)

        return render_template('index.html', colors_list = dominant_colors)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

temp_dir.cleanup()

#TODO
    # analysis - https://colab.research.google.com/drive/1loupRmuDJGitzdvMcTB7o7Etim_-bjdQ#scrollTo=Fg75QSPht7bK
    # transition after posting an image - title card goes on top, an analysis card on bottom
    # analysis card - picture on the left, top 10 colors on the right with the HEX code inside of them and their percentages

# reference: https://www.coolphptools.com/color_extract#demo
