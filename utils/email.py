# utils/email.py
from flask_mail import Mail, Message

mail = Mail()

def configure_mail(app):
    mail.init_app(app)

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='noreply@example.com'
    )
    mail.send(msg)
