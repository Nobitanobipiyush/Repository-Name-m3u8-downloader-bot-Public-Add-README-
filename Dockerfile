FROM python:3.11-slim

RUN apt update && apt install ffmpeg -y

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python app.py
