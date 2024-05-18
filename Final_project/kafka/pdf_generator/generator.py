import string
from random import choices
from producer import add_data_to_aggregated_queue
import pdfkit
from main import agregate_data
from asyncio import run
import json

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
}

def generate_pdf(msg):
    bin = msg.key().decode('utf-8')
    data = agregate_data(BIN=bin)
    file_name = generate_file_name(bin=bin)
    pdfkit.from_string(data, output_path=f'../pdfs/{file_name}', options=options)
    values = json.loads(msg.value().decode('utf-8'))
    values["bin"] = bin
    run(add_data_to_aggregated_queue(key=file_name, value=json.dumps(values)))

def generate_file_name(bin, len=20):
    return bin + '_' + ''.join(choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=len)) + '.pdf'