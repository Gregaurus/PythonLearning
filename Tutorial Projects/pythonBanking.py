#Python Banking Program

def show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter Amount to be Deposited: "))

    if amount < 0:
        print("That's not a VALID amount!")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter Amount to be Withdrawn: "))
    
    if amount > balance:
        print("Insufficient Funds!")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True
    while is_running:
        print("--------------------------------")
        print("Banking Program")
        print("--------------------------------")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        
        choice = input("Enter your choice(1-4): ")
        
        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print("--------------------------------")
                print("That is not a valid choice!")
                print("--------------------------------")
    print("--------------------------------")
    print("Thank you! Have a nice day!")
    print("--------------------------------")  

#Good Practice to make sure the program only runs if it is being run directly
if __name__ == '__main__':
    main()