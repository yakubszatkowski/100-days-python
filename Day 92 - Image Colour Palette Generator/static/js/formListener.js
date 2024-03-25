var fileInput = document.getElementById('file-upload');
var fileForm = document.getElementById('file-form');

fileInput.addEventListener('input', () => {
    fileForm.submit();
});