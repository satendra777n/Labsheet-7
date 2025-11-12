with open("file2.txt", "w") as f:
    print("Enter lines of text (type 'stop' to finish):")
    while True:
        line = input()
        if line.lower() == "stop":
            break
        f.write(line + "\n")
print("Lines written successfully.")
