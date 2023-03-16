FROM python:3.11-alpine

WORKDIR /opt/app
COPY . /opt/app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "./main.py"]