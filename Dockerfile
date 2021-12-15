FROM python:3.10

ADD requirements.txt /opt
RUN pip install -r /opt/requirements.txt

ADD . /opt
WORKDIR /opt

RUN python3 main.py