FROM python:3.8

RUN pip install requests
RUN pip install json

COPY . /app

WORKDIR /app

CMD python is_scam_website.py
