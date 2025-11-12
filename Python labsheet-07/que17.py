with open("file1.txt", "r") as f:
    lines = f.readlines()

with open("no_blank_lines.txt", "w") as f:
    for line in lines:
        if line.strip():  # skip blank lines
            f.write(line)
print("Blank lines removed successfully.")
