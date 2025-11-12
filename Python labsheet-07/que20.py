with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    data = f1.read() + "\n" + f2.read()

with open("merged.txt", "w") as f3:
    f3.write(data)

print("Files merged successfully.")
