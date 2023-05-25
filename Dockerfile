# pull official base image
FROM python:3.11.2-alpine

RUN apk update
RUN apk add make automake gcc g++ python3-dev

# set work directory
WORKDIR /usr/src/MG_RMS

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
