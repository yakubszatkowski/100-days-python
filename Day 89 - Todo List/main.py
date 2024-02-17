from flask import Flask, render_template, request

app = Flask(__name__)

task_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_task = request.form.get('task')
        if input_task:
            task_list.append(input_task)
            print(task_list)
        if request.form.get('reset_button'):
            task_list.clear()
            print(task_list)

    return render_template('index.html', tasks=task_list)


if __name__ == '__main__':
    app.run(debug=True)


#TODO
    # website reference: https://flask.io/PEhyTiWzw08V
