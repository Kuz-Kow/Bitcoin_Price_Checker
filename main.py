import requests
import json

def main():
    print(f"Current Bitcoin price is:{price(): .2f}$")

def price():
    response = requests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin")
    response = response.json()  
    price = response["quotes"]["USD"]["price"]

    return price

    
        

if __name__ == "__main__":
    main()