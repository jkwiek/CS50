import sys
import requests
while True:
    try:
        input = float(sys.argv[1])
        conversion_factor = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
    except ValueError:
        print("Command-line argument is not a number")
        break
    except IndexError:
        print("Missing command-line argument")
        break
    else:
        print(conversion_factor)
#except requests.RequestException:



