from flask import Flask, render_template, request, after_this_request
from PIL import Image
from threading import Thread
from image_processing import dominant_colors_extraction
import os, time

main_directory = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = f"{main_directory}\static\\temp_file"

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = UPLOAD_FOLDER

def delete_file(path):
    time.sleep(10)
    try:
        os.remove(path)
    except FileNotFoundError:
        path = path.replace('%20',' ')
        os.remove(path)
    return

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['picture-upload']  # kot.jpg
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
        filename = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
        pil_image = Image.open(filename)
        dominant_colors = dominant_colors_extraction(pil_image)
        
        image_wo_file_directory = filename.replace(main_directory, '.')
        formatted_image = image_wo_file_directory.replace(' ','%20')

        # workaround with threading because after_this_request decorator doesn't work on windows
        thread = Thread(target=delete_file, args=(filename,)) 
        thread.start()

        return render_template('index.html', colors_list=dominant_colors, image=formatted_image)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    

# reference: https://www.coolphptools.com/color_extract#demo
