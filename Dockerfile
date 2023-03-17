FROM python:3.10.8

WORKDIR /opt/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /opt/app

EXPOSE 8080

CMD ["python", "./main.py"]
