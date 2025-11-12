word = input("Enter word to search: ")
with open("file1.txt", "r") as f:
    content = f.read()
if word in content:
    print(f"'{word}' found in file.")
else:
    print(f"'{word}' not found in file.")
