FROM python:3.9-alpine
LABEL Auther="stdeson"
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apk add gcc python3-dev openssl-dev musl-dev libffi-dev &&\
    pip install --no-cache-dir -r requirements.txt

COPY main.py handler.py config.py ./

ENTRYPOINT ["uvicorn", "main:app", "--reload", "--port", "8080"]