FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip3 install pyTelegramBotAPI \
                  boto3

CMD ["python", "main.py"]
