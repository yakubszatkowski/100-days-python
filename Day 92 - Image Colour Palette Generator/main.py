from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        picture = request.form.get('picture-upload')
        print(picture)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


#TODO
    # post image form after choosing file
    # transition after posting an image - title card goes on top, an analysis card on bottom
    # analysis card - picture on the left, top 10 colors on the right with the HEX code inside of them - check d76

# reference: https://www.coolphptools.com/color_extract#demo
