with open("file1.txt", "r") as f:
    lines = f.readlines()
print("First line:", lines[0].strip())
print("Last line:", lines[-1].strip())
