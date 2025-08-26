#   Name: Landin Schenkel
#   Assignment: 1
#   Program Name: Loop
#   Date: 08/25/25

a = int(input("Enter the starting point: "))
b = int(input("Enter the ending point: "))
sum_odd = 0

for number in range(a, b + 1):
    if number % 2 != 0:
        sum_odd += number

print(sum_odd)