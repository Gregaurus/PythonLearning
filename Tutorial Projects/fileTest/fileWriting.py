import os
import json
import csv


file_path = "Tutorial Projects/fileTest/output.txt"
txt_data = "I like some sushi"

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

orang = {
    "name": "Spongebob",
    "age" : 30,
    "job" : "Cook"
}

person = [["Name", "Age", "Job"], 
          ["Spongebob", 30, "Cook"], 
          ["Patrick", 37, "Unemployed"], 
          ["Squidward", 59, "Cashier"]]

#FileDetection

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")
    
#     if os.path.isfile(file_path):
#         print("That is a File!")
#     elif os.path.isdir(file_path):
#         print("That is a Directory!")
# else:
#     print("That location doesn't exist")
    
#Writing and output files

# "w" = write, "r" = reading, x = write if it doesnt already exist, a = append(any new data will append)

#.txt
try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created!")
except FileExistsError:
    print("That file already exists!")

# .json
# try:
#     with open(file_path, "w") as file:
#         json.dump(orang, file, indent = 4)
#         print(f"json file '{file_path}' was created!")
# except FileExistsError:
#     print("That file already exists!")

# .csv
# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in person:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created!")
# except FileExistsError:
#     print("That file already exists!")