import os
import ccxt

# ------------------ binance ------------------
# api_key = 'b7bBgVgqzpT4Xi6g9taKn6ZwiUM8b20YL03QfhjeF0JKTGCfXgZQZjyx5VDaHD9n'
# secret = 'MwdbBUd39nkqfeXwJsY96KZtW7TqfnORb3uVQNbRnULVWE2lqs8hzApnuWZ8U4M1'

# ------------------ okx ------------------
sandbox = os.getenv('REAL_TRADING') != 'true'
api_key = os.getenv('YOUR_API_KEY_DEV') if sandbox else os.getenv('YOUR_API_KEY')
secret = os.getenv('YOUR_SECRET_DEV') if sandbox else os.getenv('YOUR_SECRET')
password = os.getenv('YOUR_PASSWORD')
print(f'api_key: {api_key}')
print(f'secret: {secret}')
print(f'password: {password}')
print(f'sandbox: {sandbox}')

