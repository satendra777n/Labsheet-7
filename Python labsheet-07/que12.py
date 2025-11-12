word = input("Enter word to count: ")
with open("file1.txt", "r") as f:
    content = f.read().split()
count = content.count(word)
print(f"'{word}' occurs {count} times.")
