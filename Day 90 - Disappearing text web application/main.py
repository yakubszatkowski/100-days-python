from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

#TODO
    #reference: https://www.squibler.io/dangerous-writing-prompt-app/write?limit=5&type=minutes