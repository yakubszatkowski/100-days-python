var tasks = document.getElementsByClassName('task')

for(var i = 0; i < tasks.length; i++) {
    const task = tasks[i]

    const edit_button = task.querySelector('.edit-task-button')
    const task_text = task.querySelector('.task-text')

    edit_button.addEventListener("click", function(event) {
        event.preventDefault()
        task_text.contentEditable = true
        task_text.focus()

    })
}