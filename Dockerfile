FROM python:3.9-alpine
LABEL Auther="stdeson"

WORKDIR /app
COPY requirements.txt ./
COPY *.py ./

RUN apk add gcc python3-dev openssl-dev musl-dev libffi-dev &&\
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["bash"]