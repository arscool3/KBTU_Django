import smtplib
from email.message import EmailMessage

def send_pdf_to_email(email, pdf_url):
    msg = EmailMessage()
    msg['Subject'] = 'Ваш PDF-документ'
    msg['From'] = 'arsennusip@gmail.com'
    msg['To'] = email

    # Скачивание PDF
    with open(f'../pdfs/{pdf_url}', 'rb') as file:
        file_data = file.read()
    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=pdf_url)

    # Отправка сообщения
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('arsennusip@gmail.com', 'hmaj fiev fxje laco')
        server.send_message(msg)