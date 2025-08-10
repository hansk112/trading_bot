import yfinance as yf
import time
from twilio.rest import Client
import json

with open('/home/hans/Repositories/trading_bot/secrets.json') as f:
    secrets = json.load(f)

# Load Twilio credentials from secrets.json
account_sid = secrets.get("account_sid", "")
auth_token = secrets.get("auth_token", "")
twilio_number = secrets.get("twilio_number","")  # Your Twilio number
recipient_number = secrets.get("recipient_number","")  # Your mobile number

print(account_sid)
print(auth_token)

# Twilio configuration
# account_sid = ""
# auth_token =  ""


client = Client(account_sid, auth_token)

# Trading configuration
ticker = "MSFT"
buy_price = 170.00
sell_price = 190.00
check_interval = 3600  # seconds

def send_sms(message):
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=recipient_number
    )

def check_price():
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")["Close"].iloc[-1]
    print(f"Current price of {ticker}: ${current_price:.2f}")

    if current_price <= buy_price:
        alert = f"📉 Buy Alert: {ticker} is at ${current_price:.2f}"
        print(alert)
        send_sms(alert)
    elif current_price >= sell_price:
        alert = f"📈 Sell Alert: {ticker} is at ${current_price:.2f}"
        print(alert)
        send_sms(alert)

while True:
    check_price()
    time.sleep(check_interval)
