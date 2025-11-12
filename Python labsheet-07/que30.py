import csv

files = ["students1.csv", "students2.csv", "students3.csv"]

with open("combined.csv", "w", newline="") as outfile:
    writer = None
    for filename in files:
        with open(filename, "r") as infile:
            reader = csv.reader(infile)
            if writer is None:
                writer = csv.writer(outfile)
            for row in reader:
                writer.writerow(row)

print("All CSV files combined successfully.")
