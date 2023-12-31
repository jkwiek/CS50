import sys
import requests

response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
conversion_factor = response.json()["bpi"]["USD"]["rate_float"]

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
else:
    n = sys.argv[1]
    cost = float(n) * conversion_factor
    print(f"${cost:,.4f}")



