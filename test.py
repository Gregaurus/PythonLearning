record = []
for _ in range(5):
    name = "rego"
    score = float(3.2)
    record.append([name,score])

print(record)
record.sort(key=lambda x: (x[1], x[0]))
print(record)
