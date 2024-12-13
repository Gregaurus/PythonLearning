# List = [] ordered and changeable, Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK, NO duplicates
# Tuple = () ordered and unchangeable, Duplicates OK. FASTER.

#Matrix

groceries = [["apple", "banana", "coconut"],
             ["celery", "broccoli"], 
             ["pork", "cow", "fish"]]

for collection in groceries:
    for items in collection:
        print(items, end=" ")
    print()