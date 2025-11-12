import csv

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    marks = [int(row["Marks"]) for row in reader]

average = sum(marks) / len(marks)
print("Average Marks:", average)
