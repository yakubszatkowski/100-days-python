from flask import Flask, render_template, request

app = Flask(__name__)

task_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_task = request.form.get('task')
        if input_task:  # add
            task_list.append(input_task)
        if request.form.get('delete_task_button'):  # delete
            task_index = int(request.form.get('task_index')) - 1
            task_list.pop(task_index)
        if request.form.get('reset_button'):  # delete all
            task_list.clear()


    return render_template('index.html', tasks=task_list)


if __name__ == '__main__':
    app.run(debug=True)


#TODO
    # edit task's text
    # warning before deliting all tasks
    # changing tasks order by click and drag
    # gratulations message when all tasks are finished

    # website reference: https://flask.io/PEhyTiWzw08V
