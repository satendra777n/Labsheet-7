old = input("Enter word to replace: ")
new = input("Enter new word: ")

with open("file1.txt", "r") as f:
    content = f.read()

content = content.replace(old, new)

with open("file1.txt", "w") as f:
    f.write(content)

print("Word replaced successfully.")
