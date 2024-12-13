import random as r

lowest_num = 1
highest_num = 100
answer = r.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("That number is out of Range!")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too Low! Try Again!")
        elif guess > answer:
            print("Too High! Try Again!")
        else:
            print(f"Correct! The Answer is {answer}")
            print(f"The number of Guesses is {guesses}")
            is_running = False
    else:
        print("Invalid Guess")
        print(f"Select a number between {lowest_num} and {highest_num}")