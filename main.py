import const
from structs import *
from utils import *
from fastapi import FastAPI, Request
import globals

app = FastAPI()

@app.post("/api/ping")
def ping():
    return "pong"


@app.post("/api/webhook")
def webhook(msg: CallBackMsg, req: Request):
    ts = get_timestamp()
    print(ts, "Alert Received & Sent!", msg)
    from_ip = req.client.host
    print(ts, "From IP:", from_ip)
    if from_ip not in const.TRADING_VIEW_IP:
        return {"code": "1", "msg": "Invalid IP"}
    if msg.key != const.TV_AUTH_KEY:
        return {"code": "2", "msg": "Invalid Key"}
    # TODO: 调用ccxt来下单
    return {
        "code": "0",
        "msg": "success"
    }
