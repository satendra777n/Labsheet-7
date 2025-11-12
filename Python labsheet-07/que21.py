import csv

data = [
    ["Name", "Marks", "Age"],
    ["Alice", 85, 20],
    ["Bob", 90, 21],
    ["Charlie", 78, 19]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV file created successfully.")
