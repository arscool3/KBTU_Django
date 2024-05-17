import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_password_email(sender_email, sender_password, recipient_email, password):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    server.login(sender_email, sender_password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Ваш пароль'

    body = "Ваш пароль: {}".format(password)
    msg.attach(MIMEText(body, 'plain'))

    server.send_message(msg)

    server.quit()
