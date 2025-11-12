import csv

new_record = ["David", 88, 22]

with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_record)

print("Record appended successfully.")
