$(document).ready(function(){
    const itemMenu = $('.stickman-items');

    if (itemMenu) {

        function ajaxPost(itemMap, image) {
            const totalLabel = $('h4#total')
    
            $.ajax({
                url: "create",
                type: "POST",
                data: {
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    ajax_data: JSON.stringify(itemMap)
                },
                success: function(response) {
                    image.attr('src', 'data:image/jpeg;charset=utf-8;base64, ' + response.stickman_image)
                    totalLabel.text('Total: $ ' + response.money_total)
                }
            });
        }

        const items = $('.stickman-items label input')
        const colorRadioButtons = $('.stickman-colors input')
        const colorLabel = $('.stickman-colors h3')
        const image = $('.stickman-picture img')
        const nameInput = $('.purchase-options input#stickman-name')
        let itemMap = {}
        let item = ''

        items.on('change', function() {
            let itemCheckbox = $(this)
            item = itemCheckbox.parent().text()

            if (itemCheckbox.is(':checked')) {
                itemMap[item] = ''
                colorRadioButtons.first().prop('checked', true).trigger('change')
                colorLabel.text(item + '\' color')
            } 
            else if (itemCheckbox.not(':checked')) {
                delete itemMap[item]
                item = Object.keys(itemMap)[Object.keys(itemMap).length-1]
                colorLabel.text(item ? item + '\' color' : 'Color')
                ajaxPost(itemMap, image)
            }
        })

        colorRadioButtons.on('change', function() {
            let choosedColor = $(this).css('background-color')
            itemMap[item] = choosedColor

            ajaxPost(itemMap, image)
        })

        nameInput.on('input', function() {
            input = nameInput.val()
            $('h1').text(input ? 'This is ' + input : 'Create your stickman')
        })
    } 
});
