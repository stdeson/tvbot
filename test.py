import os
import pytest

import requests
import time
import hmac
import base64



# 获取时间戳（UTC 时间）
def get_timestamp():
    return str(int(time.time())) + '.' + str(int(time.time() * 1000) % 1000)

# 生成签名
def generate_signature(timestamp, method, request_path, body, secret):
    message = timestamp + method.upper() + request_path + (body or "")
    hmac_key = base64.b64decode(secret)
    signature = hmac.new(hmac_key, message.encode('utf-8'), digestmod='sha256').digest()
    return base64.b64encode(signature).decode()



def test_get_asset_currencies():
    # API 密钥配置
    api_key = os.getenv('YOUR_API_KEY_DEV')
    secret = os.getenv('YOUR_SECRET_DEV')
    passphrase = os.getenv('YOUR_PASSWORD')

    # 请求地址
    url = "https://www.okx.com/api/v5/asset/currencies"
    # 请求头设置
    timestamp = get_timestamp()
    method = 'GET'
    request_path = '/api/v5/asset/currencies'
    body = ""  # GET 请求没有 body

    # 生成签名
    signature = generate_signature(timestamp, method, request_path, body, secret)

    headers = {
        'OK-ACCESS-KEY': api_key,
        'OK-ACCESS-SIGN': signature,
        'OK-ACCESS-TIMESTAMP': timestamp,
        'OK-ACCESS-PASSPHRASE': passphrase,
        'Content-Type': 'application/json'
    }

    # 发起请求
    response = requests.get(url, headers=headers, timeout=2, proxies={
        'https': 'https://127.0.0.1:11080',
        'http': 'http://127.0.0.1:11080'
    })

    # 打印返回结果
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200