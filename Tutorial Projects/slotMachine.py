#Slot Machine Game
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋","🔔","⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "🍒":
                return bet*3
            case "🍉":
                return bet*4
            case "🍋":
                return bet*5
            case "🔔":
                return bet*10
            case "⭐":
                return bet*100
    return 0

def main():
    balance = 100
    
    print("************************")
    print("Welcome to Python Slots!")
    print("Symbols: 🍒🍉🍋🔔⭐")
    print("************************")
    
    while balance > 0:
        print(f"Current Balance: ${balance:.2f}")
        
        bet = input("Place your bet amount: ")
        
        if not bet.isdigit():
            print("Please enter a VALID number! ")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient Funds!")
            continue
        
        if bet <= 0:
            print("Bet must be greater than")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}!")
            balance += payout
        else:
            print("Sorry, You Lost!")
        
        if balance <= 0:
            break
        
        play_again = input("Do you want to spin again?(Y/N): ").upper()
        if play_again != 'Y':
            break
    print("*********************************************")
    print(f"Game Over! Your final balance is: ${balance}")
    print("*********************************************")


if __name__ == '__main__':
    main()