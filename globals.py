import os
import ccxt

sandbox = os.getenv('REAL_TRADING') != 'true'
api_key = os.getenv('YOUR_API_KEY_DEV') if sandbox else os.getenv('YOUR_API_KEY')
secret = os.getenv('YOUR_SECRET_DEV') if sandbox else os.getenv('YOUR_SECRET')
password = os.getenv('YOUR_PASSWORD')
print(f'api_key: {api_key}')
print(f'secret: {secret}')
# print(f'password: {password}')
print(f'sandbox: {sandbox}')

exchange = ccxt.okx({
    'apiKey': api_key,
    'secret': secret,
    'password': password,
    'sandbox': sandbox,
    'timeout': 2,
})

# 检查连接是否正常
try:
    balance = exchange.fetch_balance({'type': 'trading'})
    print("Balance:", balance)
except Exception as e:
    print(f"Error: {str(e)}")
