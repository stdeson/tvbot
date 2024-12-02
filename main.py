import traceback
import ccxt
import const
from structs import *
from utils import *
from globals import *
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api/ping")
def ping():
    return "pong"

@app.post("/api/test")
def test():
    exchange = ccxt.okx({
        'apiKey': api_key,
        'secret': secret,
        'password': password,
        'options': {
            'defaultType': 'future',
            'sandbox': sandbox,
        },
        'timeout': 2000,
    })
    # 检查连接是否正常
    try:
        balance = exchange.fetch_balance()
        print("Balance:", balance)
        return "success"
    except Exception as e:
        traceback.print_exc()
        return "fail"



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
