FROM python:3.11-bullseye

WORKDIR /root/Mikobot

COPY . .

RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    apt-get clean

RUN pip install --upgrade pip setuptools
RUN pip install -U -r requirements.txt

CMD ["python3", "-m", "Mikobot"]
