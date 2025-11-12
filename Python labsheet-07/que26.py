import csv

with open("students.csv", "r") as f1, open("students_copy.csv", "w", newline="") as f2:
    reader = csv.reader(f1)
    writer = csv.writer(f2)
    for row in reader:
        writer.writerow(row)

print("CSV file copied successfully.")
