from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import os, tempfile

temp_dir = tempfile.TemporaryDirectory()
print(temp_dir.name)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['picture-upload']
        image.save(os.path.join(temp_dir.name, image.filename))
        filename = os.path.join(temp_dir.name, image.filename)
        pil_image = Image.open(filename)

        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

temp_dir.cleanup()

#TODO
    # analysis - https://colab.research.google.com/drive/1loupRmuDJGitzdvMcTB7o7Etim_-bjdQ#scrollTo=Fg75QSPht7bK
    # transition after posting an image - title card goes on top, an analysis card on bottom
    # analysis card - picture on the left, top 10 colors on the right with the HEX code inside of them - check d76

# reference: https://www.coolphptools.com/color_extract#demo
