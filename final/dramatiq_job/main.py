import dramatiq
from dramatiq.results.backends.redis import RedisBackend
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
import requests
from requests.exceptions import ReadTimeout

import requests
from bs4 import BeautifulSoup
import re
import os
import io
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from email.message import EmailMessage
import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.application import MIMEApplication

result_backend = RedisBackend()
broker = RedisBroker()
broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(broker)

def when_to_retry(number_of_retries: int, exc: Exception) -> bool:
    return isinstance(exc, ReadTimeout)


checks = [
    'pg13',
]

#docker run -d --name redis -p 6379:6379 redis/redis-stack-server:latest

@dramatiq.actor(store_results=True)
def send_request_to_server(name: str) -> str:
    print("ok")
    response = requests.get(f"http://127.0.0.1:9000/pg13/?name={name}")
    is_ok = not response.json()
    if not is_ok:
        return "not kid friendly"
    return "is kid friendly"

def scraping():
    url = 'https://www.nytimes.com/books/best-sellers/combined-print-and-e-book-fiction/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    names = [element.text for element in soup.find_all('h3', class_='css-5pe77f')]
    authors = [element.text for element in soup.find_all('p', class_='css-hjukut')]
    publishers = [element.text for element in soup.find_all('p', class_='css-heg334')]
    descriptions = [element.text for element in soup.find_all('p', class_='css-14lubdp')]
    img_urls = [element['src'] for element in soup.find_all('img')]
    elements=[]
    img_urls=[]
    elements=soup.find_all('img')
    result_strings = [str(element) for element in elements]
    result_as_string = ''.join(result_strings)
    url_pattern = r"https?://[^\s]+"
    img_urls = re.findall(url_pattern, result_as_string)
    img_urls = [url.split('"/><img')[0] for url in img_urls]
    print("SCRAPED")
    return names, authors, publishers, descriptions,img_urls[:-1]

def save_images(img_urls):
    image_paths = []
    print("TRYING TO SAVE")
    for index, img_url in enumerate(img_urls, start=1):
        filename = f"image_{index}.jpg"
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(os.path.join("static_resources/images", filename), 'wb') as f:
                f.write(response.content)
            print(f"Image downloaded successfully as '{filename}'")
            image_paths.append(f"static_resources/images/{filename}")
        else:
            print(f"Failed to download image {index}: HTTP status code {response.status_code}")
    return image_paths

def generate_pdf(data_arrays,image_paths):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'static_resources/fonts/DejaVuSerif.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSerif-Bold', 'static_resources/fonts/DejaVuSerif-Bold.ttf'))
    pdf.setLineWidth(1)
    
    def draw_images_on_page(pdf,image_paths, page_num):
        for i, image_path in enumerate(image_paths[page_num * 3: (page_num + 1) * 3], start=1):
            x_position = 70
            y_position = 55 + (i - 1) * 245
            width = 150
            height = 230
            pdf.drawImage(image_path, x_position, y_position, width, height)

    def write_text_on_page(pdf, data_arrays, page_num):
        start_index = page_num * 3
        for i, data_array in enumerate(data_arrays[start_index: start_index + 3], start=1):
            x_position = 240
            y_position = 255 + (i - 1) * 245
            pdf.drawString(x_position, y_position, data_array[0])  # Book title
            pdf.drawString(x_position, y_position - 25, data_array[1])  # Author
            pdf.drawString(x_position, y_position - 45, data_array[2])  # Publisher
            pdf.drawString(x_position,  y_position - 65, data_array[3])  # Description part
    for page_num in range(6):  # You have 6 pages, as per your original code
        pdf.line(55, 790, 550, 790)
        pdf.line(55, 45, 550, 45)
        pdf.line(55, 45, 55, 790)
        pdf.line(550, 45, 550, 790)

        pdf.line(45, 800, 560, 800)
        pdf.line(45, 800, 45, 35)
        pdf.line(45, 35, 560, 35)
        pdf.line(560, 800, 560, 35)

        if page_num == 0:
            pdf.setFont('DejaVuSerif-Bold', 20)
            pdf.drawString(120, 550, "The New York Times Bestsellers")
            pdf.drawString(135, 500, "Recommendations for May")
        else:
            draw_images_on_page(pdf, image_paths, page_num - 1)
            write_text_on_page(pdf, data_arrays, page_num-1)
            pdf.drawString(40, 20, f"Page {page_num }")

        if page_num < 5: 
            pdf.showPage()

    pdf.save()

    buffer.seek(0)
    # with open("output.pdf", "wb") as pdf_file:
    #     pdf_file.write(buffer.read())
    return buffer

@dramatiq.actor(store_results=True)
def send_email_after_registration(email_receiver:str):
    email_sender = 'oryn.bay505@gmail.com'
    email_password = os.environ.get("AA_EMAIL_HOST_PASSWORD")
    subject = 'Hello! You just signed up at Goodreads!'
    body = """We're glad to have you here!
            Here is The New York Time Bestsellers of this month, 
            that we recommend you to read.
            If you need any help, don't hesitate to hit us up<3 
            """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    message = MIMEMultipart()
    message.attach(MIMEText(body, "plain"))  

    names, authors, publishers, descriptions, img_urls= scraping()
    data_arrays = list(zip(names, authors, publishers, descriptions))
    image_paths=save_images(img_urls)

    pdf_attachment = MIMEApplication(generate_pdf(data_arrays,image_paths).getvalue(), 'pdf')
    pdf_attachment.add_header('Content-Disposition', 'attachment', filename=f'the_nyt_bestsellers.pdf')
    message.attach(pdf_attachment)

    message["Subject"] = subject
    message["From"] = email_sender
    message["To"] = email_receiver

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, [email_receiver], message.as_bytes())
    return "Greeting email send succesfully"



@dramatiq.actor(store_results=True)
def send_pdf(chat_id: str):
    token = os.environ.get("TG_API_TOKEN")
    names, authors, publishers, descriptions, img_urls = scraping()
    data_arrays = list(zip(names, authors, publishers, descriptions))
    image_paths = save_images(img_urls)

    pdf_attachment = generate_pdf(data_arrays, image_paths)

    caption = 'Your recommendation list for May'

    url_doc = f'https://api.telegram.org/bot{token}/sendDocument'

    files = {'document': ('recommendations.pdf', pdf_attachment, 'application/pdf')}

    params = {'chat_id': chat_id, 'caption': caption}
    try:
        response = requests.post(url_doc, files=files, params=params)
        response.raise_for_status()  # raise an exception for any HTTP error
    except requests.exceptions.RequestException as e:
        # Handle any request exceptions here
        print("Request error:", e)
    else:
        return response

