import sys
import json
import requests

response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
response = response.json()
conversion_factor = response["rate_float"]

while True:
    try:
        USD = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        break
    except IndexError:
        print("Missing command-line argument")
        break
bitcoin
#except requests.RequestException:



