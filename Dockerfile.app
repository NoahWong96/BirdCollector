FROM python:3.8-slim-buster

COPY /Source /Source

WORKDIR /Source

EXPOSE 8080

RUN pip install Pillow
RUN pip install flask

ENTRYPOINT FLASK_APP=/application.py flask run --host=0.0.0.0