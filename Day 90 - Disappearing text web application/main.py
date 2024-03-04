from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

#TODO
    # change textarea by colors, boxShadow, blur style variables based on timeElapsed value

    # reference: https://www.squibler.io/dangerous-writing-prompt-app/write?limit=5&type=minutes
