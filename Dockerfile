FROM python:3.10.8-alpine

WORKDIR /opt/app
COPY . /opt/app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "./main.py"]
