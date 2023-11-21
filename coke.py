#Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts
#25 cents, 10 cents, and 5 cents.
#insert a coin, one at a time, each time informing the user of the amount due.
#Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
#Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
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

print("Change Owed:", coinsum - 50)
