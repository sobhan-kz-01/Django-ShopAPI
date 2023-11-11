FROM python:3.12-slim

RUN mkdir /app

ENV DJANGO_SUPERUSER_PASSWORD admin

WORKDIR /app
COPY requirements.txt /app
# RUN apt-get update \
#     && apt-get -y install libpq-dev gcc 
    
RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY requirements.txt /app


CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user admin --email email@gmail.com --noinput ;\