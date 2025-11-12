import csv

name = input("Enter student name to search: ")

found = False
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Name"].lower() == name.lower():
            print("Record found:", row)
            found = True
            break

if not found:
    print("Record not found.")
