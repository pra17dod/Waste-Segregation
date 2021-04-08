FROM python:3.8-slim-buster
FROM tensorflow/tensorflow:2.3.0
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]