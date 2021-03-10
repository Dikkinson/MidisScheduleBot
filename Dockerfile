FROM python:3.8

WORKDIR /home

COPY requirements.txt ./
RUN pip install -U pip install -r requirements.txt && apt-get update
COPY ./ ./

ENTRYPOINT ["python", "app.py"]