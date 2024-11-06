const item_menu = document.querySelector('.stickman-items');


if (item_menu) {
    const items = item_menu.querySelectorAll('li')
    const color_label = document.querySelector('.stickman-colors h3')
    const color_radio_buttons = document.querySelectorAll('.stickman-colors input')

    for (let i = 0; i<items.length; i++) {
        items[i].addEventListener('click', () => {
            let item = items[i].innerText
            color_label.innerText = item + '\'s color'
            color_radio_buttons[0].checked = true
        })
    }
} 
