from flask import Flask, render_template, request

app = Flask(__name__)

task_list = ['buy milk', 'go for a walk', 'take a shower', 'go bed early']

@app.route('/', methods=['GET', 'POST'])
def index():
    global task_list
    if request.method == 'POST':
        input_task = request.form.get('task')
        edited_task = request.form.get('edit_task_input')
        new_task_order = request.form.get('new_task_list')
        
        try:
            task_index = int(request.form.get('task_index')) - 1
        except TypeError:
            pass

        if input_task:  # add task
            task_list.append(input_task)
        elif request.form.get('delete_task_button'):  # delete task
            task_list.pop(task_index)
        elif edited_task:  # edit task
            task_list[task_index] = edited_task
            print(task_list)
        elif request.form.get('reset_button'):  # delete all tasks
            task_list.clear()
        elif new_task_order:  # new tasks order
            new_task_list = new_task_order.split(',')
            task_list = new_task_list
            
    return render_template('index.html', tasks=task_list)


if __name__ == '__main__':
    app.run(debug=True)


#TODO
    # implement onEnd functionality update list order and submit it
        
    # warning before deliting all tasks
    # gratulations message when all tasks are finished

    # store data as cookies?
    # website reference: https://flask.io/PEhyTiWzw08V
