FROM python:3.8.3-alpine
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add libffi-dev build-base postgresql-dev gcc python3-dev musl-dev bash
RUN pip install --upgrade pip
RUN pip install Django>=3.0 djangorestframework psycopg2 tzdata django-cors-headers django-request-logging requests drf_yasg