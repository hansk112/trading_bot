import json
import os


with open('/home/hans/Documents/trading_bot/secrets.json') as f:
    secrets = json.load(f)

# Load Twilio credentials from secrets.json
account_sid = secrets.get("account_sid", "")
auth_token = secrets.get("auth_token", "")

print(account_sid)
print(auth_token)