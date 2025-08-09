import yfinance as yf
import time
from twilio.rest import Client

# Twilio configuration
account_sid = "AC0fa5e66f3dc7c7d1d872d9d9e22e04fe"
auth_token = "4e5eb9ef998c5ffe349cb2bb1640b6df"
twilio_number = "+64d221009858"  # Your Twilio number
recipient_number = "+64221009858"  # Your mobile number

client = Client(account_sid, auth_token)

# Trading configuration
ticker = "AAPL"
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
