# syntax = docker/dockerfile:1.2
FROM python:3.9

WORKDIR /realtime-tunes

COPY . .

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common 

RUN pip3 install --no-cache-dir -r requirements.txt


CMD [ "python3", "./realtime_tunes/app.py" ]