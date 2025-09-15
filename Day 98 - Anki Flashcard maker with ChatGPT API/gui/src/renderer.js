import $ from 'jquery';

const form = $('#input-form')
const chooseFileButton = $('#choose-file-button')
const filePathInput = $('#input-file-path')
const chooseDirectoryButton = $('#choose-directory-button')
const fileDirectoryInput = $('#input-directory-path')

chooseFileButton.on('click', async (e) => {
    var path = await openFileApi.openFile()
    filePathInput.val(path)
})

chooseDirectoryButton.on('click', async (e) => {
    var path = await saveDirectoryApi.saveDirectory()
    fileDirectoryInput.val(path)
})

form.on('submit', (e) => {
    e.preventDefault()
    var formData = $(e.target).serializeArray()
    var filePathInputValue = filePathInput.val()

    if (filePathInputValue.search('.pdf') > 0) {
        sendData.toMain(formData)
    } else {
        showError.toMainError()
    }
})
