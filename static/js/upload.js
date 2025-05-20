// static/js/upload.js
document.getElementById('upload-form').onsubmit = function(event) {
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];
    if (file) {
        // 处理文件上传逻辑
        console.log('Uploading file:', file.name);
    }
    event.preventDefault();
};
