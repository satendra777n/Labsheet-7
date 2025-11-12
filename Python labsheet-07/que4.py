with open("file1.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Number of words:", len(words))
