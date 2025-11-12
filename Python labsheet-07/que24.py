import csv

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)
    row_count = len(rows)
    col_count = len(rows[0]) if rows else 0

print("Rows:", row_count)
print("Columns:", col_count)
