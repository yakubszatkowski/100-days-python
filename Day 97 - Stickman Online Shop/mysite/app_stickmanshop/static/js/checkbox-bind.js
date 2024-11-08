const itemMenu = $('.stickman-items');

if (itemMenu) {

    const items = $('.stickman-items label')
    const colorLabel = $('.stickman-colors h3')
    const colorRadioButtons = $('.stickman-colors input')
    const form = $('#creator-form')
    let item = ''
    let choosedColor = ''

    items.on('click', function() {
        item = $(this).text();
        colorLabel.text(item + '\'s color')
        colorRadioButtons.first().prop('checked', true).trigger('change')
    });

    colorRadioButtons.on('change', function() {
        choosedColor = $(this).css('background-color')
        finalItem = item + ': ' + choosedColor

        $.ajax({
            url: "create",
            type: "POST",
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                'finalItem': finalItem
            },
        });
    })
} 