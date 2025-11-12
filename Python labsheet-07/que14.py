with open("file1.txt", "r") as f:
    lines = f.readlines()
longest = max(lines, key=len)
print("Longest line:", longest)
