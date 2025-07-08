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
    
    console.log(formData)
})
