var tasks = document.getElementsByClassName('task');
var enterEvent = new KeyboardEvent('keydown', { key: 'Enter', keyCode: 13 });

const submitInput = (event) => {
    if (event.key == 'Enter')
}

const createInput = (text, event) => {
    event.preventDefault();
    var string_value = text.textContent;

    var edit_input = document.createElement('input');
    edit_input.type = 'text';
    edit_input.value = string_value
    edit_input.classList.add('task-text', 'edit-text')
    edit_input.name = 'edit_task_input'

    text.parentNode.replaceChild(edit_input, text)

    text.addEventListener('keypress', function(event) {
        submitInput(event)
    })
}

for (var i = 0; i < tasks.length; i++) {
    const task = tasks[i];

    const edit_button = task.querySelector('.edit-task-button');
    const task_text = task.querySelector('.task-text');

    edit_button.addEventListener("click", function (event) {
        createInput(task_text, event);
    });
}
