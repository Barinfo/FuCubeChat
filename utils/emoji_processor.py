# utils/emoji_processor.py
import os
import random
import string
from PIL import Image

class EmojiProcessor:
    EMOJI_DIR = 'static/emoji/users'
    MAX_SIZE = 384 * 1024  # 384KB
    RESOLUTION_LIMIT = (512, 512)

    @staticmethod
    def generate_filename():
        timestamp = int(time.time())
        rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        return f"{timestamp}_{rand_str}"

    def process_upload(self, file):
        ext = file.filename.split('.')[-1].lower()
        filename = f"{self.generate_filename()}.{ext}"
        save_path = os.path.join(self.EMOJI_DIR, filename)

        if ext in ['png', 'jpg', 'jpeg']:
            img = Image.open(file)
            img.thumbnail(self.RESOLUTION_LIMIT)
            img.save(save_path, optimize=True, quality=85)
        elif ext == 'gif':
            file.save(save_path)  # GIF 不处理

        return {
            'filename': filename,
            'path': save_path,
            'is_gif': ext == 'gif',
            'size': os.path.getsize(save_path),
            'width': img.width if ext in ['png', 'jpg', 'jpeg'] else None,
            'height': img.height if ext in ['png', 'jpg', 'jpeg'] else None
        }
