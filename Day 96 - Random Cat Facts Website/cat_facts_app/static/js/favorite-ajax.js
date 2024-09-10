$('#custom-checkbox').on('change', function() {
    let isChecked = $(this).is(':checked');  
    let catID = $('#cat-id').val()
    $.ajax({
        type: 'POST',
        data: {
            task: isChecked,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            cat_id: catID,
        },
    });
});