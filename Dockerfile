FROM python:3.7.9

WORKDIR /opt/app
COPY . /opt/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "./main.py"]
