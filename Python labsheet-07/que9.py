with open("file1.txt", "r") as f1, open("file_copy.txt", "w") as f2:
    f2.write(f1.read())
print("File copied successfully.")
