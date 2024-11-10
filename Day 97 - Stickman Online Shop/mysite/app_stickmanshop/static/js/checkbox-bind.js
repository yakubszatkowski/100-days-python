const itemMenu = $('.stickman-items');

function ajaxPost(itemMap) {
    console.log(itemMap)

    $.ajax({
        url: "create",
        type: "POST",
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            ajax_data: JSON.stringify(itemMap)
        },
        // success: function(response) {
        //     image.attr('src', 'data:image/jpeg;charset=utf-8;base64, ' + response.stickman_image)
        // }
    });
}

if (itemMenu) {
    const items = $('.stickman-items label input')
    const colorRadioButtons = $('.stickman-colors input')
    const colorLabel = $('.stickman-colors h3')
    let itemMap = {}
    let item = ''

    items.on('change', function() {
        let itemCheckbox = $(this)
        item = itemCheckbox.parent().text()

        if (itemCheckbox.is(':checked')) {
            itemMap[item] = ''
            colorRadioButtons.first().prop('checked', true).trigger('change')
            colorLabel.text(item + '\'s color')
        } 
        else if (itemCheckbox.not(':checked')) {
            delete itemMap[item]
            item = Object.keys(itemMap)[Object.keys(itemMap).length-1]
            colorLabel.text(item ? item + '\'s color' : 'Color')
            ajaxPost(itemMap)
        }
    })

    colorRadioButtons.on('change', function() {
        let choosedColor = $(this).css('background-color')
        itemMap[item] = choosedColor

        ajaxPost(itemMap)
    })
} 