with open("file1.txt", "r") as f:
    lines = f.readlines()
    for i in range(1, len(lines), 2):  # 0-indexed, so 1 means 2nd line
        print(lines[i], end="")
