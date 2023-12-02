FROM python:3.11.6-bookworm
WORKDIR .

COPY . .

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN pip install -r requirements.txt
EXPOSE 9009

CMD ["python", "server.py", "--port=9009"]