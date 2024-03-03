from flask import Flask, render_template, request, make_response
import json

app = Flask(__name__)


def get_tasks():
    tasks_cookie = request.cookies.get('task_list')
    if tasks_cookie:
        return json.loads(tasks_cookie)
    else:
        return []


@app.route('/', methods=['GET', 'POST'])
def index():
    task_list = get_tasks()
    if request.method == 'POST':
        input_task = request.form.get('task')
        edited_task = request.form.get('edit_task_input')
        new_task_order = request.form.get('new_task_list')
        
        try:
            task_index = int(request.form.get('task_index')) - 1
        except TypeError:
            pass

        if input_task:  # add task
            input = [input_task, False]
            task_list.append(input)
            print(task_list)
        elif request.form.get('delete_task_button'):  # delete task
            task_list.pop(task_index)
        elif edited_task:  # edit task
            task_list[task_index][0] = edited_task
        elif request.form.get('reset_button'):  # delete all tasks
            task_list.clear()
        elif new_task_order:  # new tasks order
            new_task_list = []
            new_list = new_task_order.split(',')
            for i in range(0, len(new_list), 2):
                boolean_item = (True if new_list[i+1] == 'true' else False)
                new_task_list.append([new_list[i], boolean_item])
            task_list = new_task_list

        response = make_response(render_template('index.html', tasks=task_list))
        print(json.dumps(task_list))
        response.set_cookie('task_list', json.dumps(task_list))
        return response
            
    return render_template('index.html', tasks=task_list)


if __name__ == '__main__':
    app.run(debug=True)

