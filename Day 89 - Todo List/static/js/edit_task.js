var tasks = document.getElementsByClassName('task-form');

const createInput = (text, event) => {
    event.preventDefault();

    var edit_input = document.createElement('input');
    edit_input.type = 'text';
    edit_input.value = text.textContent;
    edit_input.classList.add('task-text', 'edit-text')
    edit_input.name = 'edit_task_input'
    
    text.parentNode.replaceChild(edit_input, text)
    edit_input.focus()

    edit_input.addEventListener('keypress', event => {
        if (event.key === 'Enter') {
            const form = event.target.parentNode
            form.submit();
    }})

    edit_input.addEventListener('focusout', event => {
        const form = event.target.parentNode
        form.submit();
    })
}

for (var i = 0; i < tasks.length; i++) {
    const task = tasks[i];
    const edit_button = task.querySelector('.edit-task-button');
    const task_text = task.querySelector('.task-text');

    edit_button.addEventListener('click', function (event) {
        createInput(task_text, event);
    });
}

