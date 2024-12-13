import random

options = ("rock", "paper", "scissors")
is_playing = True

while is_playing:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice(rock | paper | scissors): ")

    print(f"Player {player}")
    print(f"Computer {computer}")

    if player == computer:
        print("It's a TIE! ")
    elif player == "rock" and computer == "scissors":
        print("You WIN! ")
    elif player == "paper" and computer == "rock":
        print("You WIN! ")
    elif player == "scissors" and computer == "paper":
        print("You WIN! ")
    else:
        print("You LOSE! ")
        
    if not input("Play Again?(y/n): ").lower() == "y":
        is_playing = False
        
print("Thanks for Playing! ")