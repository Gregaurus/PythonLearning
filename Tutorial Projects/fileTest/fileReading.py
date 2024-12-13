import json
import csv

file_path = "Tutorial Projects/fileTest/output.csv"


#txt file
# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found!")
# except PermissionError:
#     print("You don't have permission for that file!")
    
#json file
# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content["name"])
# except FileNotFoundError:
#     print("That file was not found!")
# except PermissionError:
#     print("You don't have permission for that file!")
    
#csv file
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You don't have permission for that file!")