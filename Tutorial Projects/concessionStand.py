#Concession stand Program

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 2.50,
    "fries": 4.00,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.20
}

cart = []
total = 0

print("----------------- Menu -----------------") 
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------------------------")

while True:
    food = input("Select an Item(q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print("----------------- Your Order -----------------")
print(f"Your total is: ${total:.2f}")