# Python Quiz Game

questions = ("Your dog name?", 
             "Your name?", 
             "Your first game?")

options = (("A. Moggie",
            "B. Powie",
            "C. Mika",
            "D. Bobo"), 
           ("A. Biboo",
            "B. Kaela",
            "C. Alisha",
            "D. Demon"), 
           ("A. Barbie",
            "B. Shrek",
            "C. Pokemon",
            "D. Bocah Petualang"))
answers = ("B", "B", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------")
    print(question)
    for  option in options[question_num]:
        print(option)
    
    guess = input("Enter your Answer(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1

print("---------------------------")
print("          RESULTS          ")
print("---------------------------")

print("Answers: ", end ="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end ="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your Score is: {score}%")