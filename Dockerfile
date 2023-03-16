FROM python:3.7.9-alpine

WORKDIR /opt/app
COPY . /opt/app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "./main.py"]
