FROM python:3.9-alpine
LABEL Auther="stdeson"

WORKDIR /app
COPY requirements.txt ./
COPY *.py ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
