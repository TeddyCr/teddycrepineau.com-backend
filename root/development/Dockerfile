FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

RUN pip install --upgrade pip
ADD /root/requirements.txt /app/

WORKDIR /app/

RUN pip install -r requirements.txt \
    && 

ADD . /app/

RUN chmod +x ./root/start.sh