FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /src
EXPOSE 8000