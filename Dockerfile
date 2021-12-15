FROM python:3.10

ADD requirements.txt /opt
RUN pip install -r /opt/requirements.txt

ADD . /opt
WORKDIR /opt

RUN git config --global user.email "root@localhost"
RUN git config --global user.name "Substitutionplan Retention System"

CMD [ "python", "main.py" ]