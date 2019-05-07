FROM python:3.7

MAINTAINER davidpierrea

ENV PYTHONUNBUFFERED 1

COPY . /app/

WORKDIR /app

RUN pip install pipenv

RUN pipenv install --dev

EXPOSE 8000

CMD [ "pipenv", "run", "python", "./manage.py", "runserver", "0.0.0.0:8000" ]