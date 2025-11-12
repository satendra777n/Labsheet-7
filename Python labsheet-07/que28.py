import csv

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    max_marks = -1
    top_student = ""
    for row in reader:
        if int(row["Marks"]) > max_marks:
            max_marks = int(row["Marks"])
            top_student = row["Name"]

print(f"Top Student: {top_student}, Marks: {max_marks}")
