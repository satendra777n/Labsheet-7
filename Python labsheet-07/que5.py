with open("file1.txt", "r") as f:
    lines = f.readlines()
    line_count = len(lines)
    char_count = sum(len(line) for line in lines)
    print("Lines:", line_count)
    print("Characters:", char_count)
