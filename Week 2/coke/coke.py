coinsum = 0
coins = [5,10,25]

while coinsum < 50:
    coin = int(input("Insert Coin: "))
    if coin in coins:
        coinsum += coin
        remainder = 50 - coinsum
        if remainder < 0:
            remainder = 0
        print ("Amount Due:", remainder)
    else:
        print("Amount Due:", 50 - coinsum)

print("Change Owed:", coinsum - 50)
