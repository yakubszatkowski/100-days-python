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

const getDragAfterElement = (container, y) => {
    const draggable_elements = [...container.querySelectorAll('.draggable:not(.dragging)')]
    return draggable_elements.reduce( (closest, child) => {
        const box = child.getBoundingClientRect()
        const offset = y - box.top - box.height / 2
        if (offset < 0 && offset > closest.offset) {
            return { offset: offset, element: child}
        } else {
            return closest
        }
    }, { offset: Number.NEGATIVE_INFINITY }).element
}

for (var i = 0; i < tasks.length; i++) {
    const task = tasks[i];
    const edit_button = task.querySelector('.edit-task-button');
    const task_text = task.querySelector('.task-text');

    edit_button.addEventListener('click', function (event) {
        createInput(task_text, event);
    });

    task.addEventListener('dragstart', () => {
        task.classList.add('dragging')
    })

    task.addEventListener('dragend', () => {
        task.classList.remove('dragging')
    })

    task_container.addEventListener('dragover', (event) => {
        event.preventDefault();
        const afterElement = getDragAfterElement(task_container, event.clientY);
        const draggable = document.querySelector('.dragging');
        if (afterElement == null) {
            task_container.appendChild(draggable);
        } else {
            task_container.insertBefore(draggable, afterElement);
        }
    });
}




