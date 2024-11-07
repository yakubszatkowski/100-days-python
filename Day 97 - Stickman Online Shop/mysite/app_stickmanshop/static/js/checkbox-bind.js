const itemMenu = document.querySelector('.stickman-items');


if (itemMenu) {

    const items = itemMenu.querySelectorAll('label') // change to input and grab parent?
    const coloLabel = document.querySelector('.stickman-colors h3')
    const colorRadioButtons = document.querySelectorAll('.stickman-colors input')
    let item = ''
    let choosedColor = ''

    for (let i = 0; i < items.length; i++) {
        items[i].addEventListener('click', () => {
            item = items[i].innerText
            coloLabel.innerText = item + '\'s color'
            colorRadioButtons[0].checked = true
            console.log(item + ': rgb(255, 255, 255)')    
        })
    }

    for (let j = 0; j < colorRadioButtons.length; j++) {
        colorRadioButtons[j].addEventListener('change', () => {
            choosedColor = getComputedStyle(colorRadioButtons[j])['background-color']
            let itemAndColor = item + ': '+ choosedColor
            console.log(itemAndColor)
            
        })
    }

    

    
} 
