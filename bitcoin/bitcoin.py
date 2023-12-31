import sys
import requests

response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
conversion_factor = response.json()["bpi"]["USD"]["rate_float"]
#conversion_factor = response["bpi"]
#conversion_factor = conversion_factor["USD"]
#conversion_factor = conversion_factor["rate_float"]


if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit
try:
    n = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit
else:
    n = sys.argv[1]
    cost = float(n) * conversion_factor
    print(f"${cost:,.4f}")

#except requests.RequestException:

#BPI->USD->rate_float


