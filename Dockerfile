FROM python:3.11-bullseye

WORKDIR /root/Mikobot

COPY . .

# System deps
RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    apt-get clean

# Python tooling
RUN pip install --upgrade pip setuptools wheel

# 🔥 CRITICAL FIX: pin numpy BEFORE requirements
RUN pip install "numpy<2"

# Install project deps
RUN pip install -U -r requirements.txt

CMD ["python3", "-m", "Mikobot"]
