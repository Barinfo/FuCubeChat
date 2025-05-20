# utils/captcha.py
from captcha.image import ImageCaptcha
import random
import string

def generate_captcha(text=None):
    if text is None:
        text = ''.join(random.choices(string.digits, k=4))  # 生成4位随机数字
    image = ImageCaptcha()
    data = image.generate(text)
    image.write(text, 'static/captchas/{}.png'.format(text))  # 保存验证码图像
    return text
