import requests
import sys

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except (requests.RequestException, KeyError) as e:
        print("Error occurred while fetching Bitcoin price:", str(e))
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Invalid number of bitcoins.")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_price = bitcoins * bitcoin_price

    formatted_price = "{:,.4f}".format(total_price)
    print(f"The current price of {bitcoins} bitcoin(s) is ${formatted_price} USD.")

if __name__ == "__main__":
    main()