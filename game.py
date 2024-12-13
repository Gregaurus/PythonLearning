import random as r

balance = 100


while balance > 0:
    print("\nbalance: " +str(balance))
    card = r.randint(1,10)
    print("\nthe number is: " +str(card))
    try:
        bet = int(input("Input your bet: ")) 
    except ValueError:
        print("Input a Valid Number!")
        continue
    if bet > balance:
        print("You don't have enough balance")
        continue
    while True:
        a = input("higher, lower, or equal?\n") 
        b = r.randint(1,10)
        match a:
            case "higher":
                print("\nTheir number is: " +str(b))
                if b>card:
                    balance += bet
                    print("You Win!")
                else:
                    balance -= bet
                    print("You Lost!")
                break
            case "lower":
                print("\nTheir number is: " +str(b))
                if b<card:
                    balance += bet
                    print("You Win!")
                else:
                    balance -= bet
                    print("You Lost!")
                break
            case "equal":
                print("\nTheir number is: " +str(b))
                if b==card:
                    balance += bet
                    print("You Win!")
                else:
                    balance -= bet
                    print("You Lost!")
                break
            case _:
                print("\nPick between the three cases!")
else:
    print("\nyour balance is: " +str(balance))
    print("BANKRUPT")

