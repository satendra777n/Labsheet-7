with open("file1.txt", "r") as f:
    words = f.read().split()

unique_words = sorted(set(words))

with open("unique_words.txt", "w") as f:
    f.write(" ".join(unique_words))

print("Unique words stored successfully.")
