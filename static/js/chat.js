// static/js/chat.js
document.addEventListener('DOMContentLoaded', () => {
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');

    messageForm.onsubmit = function(event) {
        event.preventDefault();
        const message = messageInput.value;
        // 发送消息逻辑
        console.log('Sending message:', message);
        messageInput.value = '';
    };
});
