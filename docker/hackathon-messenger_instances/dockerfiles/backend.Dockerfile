FROM registry.gitlab.com/ignatinyutsin/mtg-ladder/base-django-app:latest
RUN pip install --upgrade pip
COPY ./backend/api/requirements.txt .
RUN pip install -r requirements.txt

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
COPY ./backend/api/ .
