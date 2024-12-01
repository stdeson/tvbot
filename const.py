import os
# TV官方IP, 只会从这些IP发消息回调我们的API
TRADING_VIEW_IP = [
    '52.89.214.238', '34.212.75.30', '54.218.53.128', '52.32.178.7'
]

# 访问密钥, 自定义你的
TV_AUTH_KEY = os.getenv('TV_AUTH_KEY', 'your_auth_key')