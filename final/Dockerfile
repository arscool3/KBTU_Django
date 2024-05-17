FROM python:3.10
WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt.txt


EXPOSE 8000

ENV NAME World

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]