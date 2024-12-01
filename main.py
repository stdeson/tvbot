
import time
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp

@app.post("/api/ping")
def ping():
    return {
        "code": "0",
        "msg": "pong"
    }

class WebHookReq(BaseModel):
    key: str


@app.post("/api/webhook")
def webhook(req: WebHookReq):
    print(get_timestamp(), "Alert Received & Sent!", req)
    return {
        "code": "0",
        "msg": "success"
    }
