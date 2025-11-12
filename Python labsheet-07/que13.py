with open("numbers.txt", "r") as f:
    numbers = [float(num) for num in f.read().split()]
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)
