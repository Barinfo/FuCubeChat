// static/js/emoji.js
document.addEventListener('DOMContentLoaded', () => {
    const emojiButton = document.getElementById('emoji-button');
    const emojiPicker = document.getElementById('emoji-picker');

    emojiButton.onclick = function() {
        emojiPicker.classList.toggle('show');
    };
});
