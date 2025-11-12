with open("file1.txt", "r") as f:
    words = f.read().split()

words.sort()

with open("sorted_words.txt", "w") as f:
    f.write(" ".join(words))

print("Words sorted and saved successfully.")
