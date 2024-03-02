var tasks = document.getElementsByClassName('task-form');
var task_container = document.getElementById('task-container')

const createInput = (text, event) => {
    event.preventDefault();

    var edit_input = document.createElement('input');
    edit_input.type = 'text';
    edit_input.value = text.textContent;
    edit_input.classList.add('task-text', 'edit-text');
    edit_input.name = 'edit_task_input';
    
    text.parentNode.replaceChild(edit_input, text);
    edit_input.focus();

    edit_input.addEventListener('keypress', event => {
        if (event.key === 'Enter') {
            const form = event.target.parentNode
            form.submit();
    }});

    edit_input.addEventListener('focusout', event => {
        const form = event.target.parentNode;
        form.submit();
    });
}

const submitNewList = (event) => {
    var new_tasks_sort = document.getElementsByClassName('task-text');
    var hidden_form = document.getElementById('hidden-form')
    var new_task_list = [];
    for(let item of new_tasks_sort) {
        text = item.textContent;
        new_task_list.push(text);
    };
    
    const hidden_list = document.createElement('input');
    hidden_list.type = 'hidden';
    hidden_list.name = 'new_task_list'
    hidden_list.value = new_task_list

    hidden_form.appendChild(hidden_list);
    hidden_form.submit()
}

for (var i = 0; i < tasks.length; i++) {
    const task = tasks[i];
    const edit_button = task.querySelector('.edit-task-button');
    const task_text = task.querySelector('.task-text');

    edit_button.addEventListener('click', function (event) {
        createInput(task_text, event);
    });
}

new Sortable(task_container, {
    animation: 150,
    chosenClass: "sortable-chosen",
    dragClass: "sortable-drag",
    handle: ".drag-drop-icon",
    onEnd: function(event) {
        submitNewList(event);
    },
});
