var checkboxes = document.getElementsByClassName('checkbox')

const checkboxesChecked = () => {
    for (var i = 0; i < checkboxes.length; i++) {
        if (!checkboxes[i].checked) {
            return false;
        }
    }
    return true;
}

const showAlert = () => {
    if (checkboxesChecked()) {
        alert('Congratulations! You\'ve finished all tasks!');
    }
}

for (var i = 0; i < checkboxes.length; i++) {
    checkboxes[i].addEventListener('click', showAlert);
}