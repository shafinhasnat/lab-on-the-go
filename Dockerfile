FROM python:3.9.5-slim-buster
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
VOLUME /hostpipe
COPY . .
CMD python3 app.py