# syntax = docker/dockerfile:1.2
FROM python:3.9

WORKDIR /realtime-tunes

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY realtime-tunes ./realtime-tunes/


ENV PYTHONPATH "${PYTHONPATH}:/realtime_tunes"
CMD [ "python", "./realtime_tunes/app.py" ]