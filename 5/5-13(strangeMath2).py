number = 1
sum = 0
while (number < 1000):
    if ((number % 2) == 0 or (number % 3) == 0):
        sum += number
    number += 1

print(sum)