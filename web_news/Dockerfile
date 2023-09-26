FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    apt-get clean

WORKDIR /app
COPY . /app

EXPOSE 8000

CMD ["make", "server"]
