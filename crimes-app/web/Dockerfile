FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-dev python3-pip nginx
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run"]
