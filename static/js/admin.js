// static/js/admin.js
document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.delete-button');
    deleteButtons.forEach(button => {
        button.onclick = function() {
            const userId = this.dataset.userId;
            // 处理删除用户逻辑
            console.log('Deleting user with ID:', userId);
        };
    });
});
