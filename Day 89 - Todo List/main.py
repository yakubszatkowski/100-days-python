from flask import Flask, render_template, request

app = Flask(__name__)
task_list = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_task = request.form.get('task')
        if input_task:  # add task
            task_list.append(input_task)
        elif request.form.get('delete_task_button'):  # delete task
            task_index = int(request.form.get('task_index')) - 1
            task_list.pop(task_index)
        elif request.form.get('reset_button'):  # delete all tasks
            task_list.clear()
            
    return render_template('index.html', tasks=task_list)


if __name__ == '__main__':
    app.run(debug=True)


#TODO
    # edit task
        # js - add event listener
    # changing tasks order by click and drag
    # warning before deliting all tasks
    # gratulations message when all tasks are finished

    # website reference: https://flask.io/PEhyTiWzw08V
