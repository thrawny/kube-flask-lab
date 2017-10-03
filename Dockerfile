FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /src
WORKDIR /src

COPY requirements.txt /src/
RUN mkdir -p /pip-sources
RUN cd /pip-sources && pip install --no-cache-dir -r /src/requirements.txt

COPY . /src/
