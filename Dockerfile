FROM python:3

WORKDIR /src

COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY . /src/