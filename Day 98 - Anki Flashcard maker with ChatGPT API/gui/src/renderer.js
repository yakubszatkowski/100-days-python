import $ from 'jquery';

const form = $('#input-form')
const chooseFileButton = $('#choose-file-button')
const filePathInput = $('#input-file-path')

chooseFileButton.on('click', async (e) => {
    var path = await openFileApi.openFile()
    filePathInput.val(path)
})

form.on('submit', (e) => {
    e.preventDefault()
    var formData = $(e.target).serializeArray()
    var filePathInputValue = filePathInput.val()

    if (filePathInputValue.search('.pdf') > 0) {
        sendData.toMain(formData)
    } else {
        console.log('error')
        // TODO: ERROR DIALOG HERE
    }
})
