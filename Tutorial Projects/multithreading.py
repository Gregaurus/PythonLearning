#Multithreading = perform multiple tasks concurrently, Good for I/O bound tasks like reading files or fetching data from APIs

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")


# # one by one
# walk_dog()
# take_out_trash()
# get_mail()

# concurrently - multithreading
# MAKE SURE args always have ',' to let the code know its a tuple
chore1 = threading.Thread(target=walk_dog, args=("Spongebob", "Squarepants"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

#waiting for the threads to finish before continuing the code/program
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")