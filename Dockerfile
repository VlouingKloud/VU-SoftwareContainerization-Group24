FROM ubuntu
RUN apt update
RUN apt dist-upgrade -y
RUN apt install -y software-properties-common
RUN add-apt-repository universe
RUN apt update
RUN apt install -y python3 python3-pip python3-psycopg2

COPY ./requirements.txt .
COPY ./server.py .
COPY ./bottle.py .

EXPOSE 8000
CMD ["python3", "server.py"]
