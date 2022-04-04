FROM python:3.8-slim-buster

COPY /Data /Data
COPY /Source /Source

WORKDIR /Source

RUN pip install Pillow

CMD [ "python", "BirdVisualizer.py"]
