# task 8
# Sum of First N Natural Numbers

N = int(input("Enter a number: "))
total = 0
for i in range(1, N + 1):
    total += i
print("Sum:", total)