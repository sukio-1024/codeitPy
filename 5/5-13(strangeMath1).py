number = 1
while (number <= 100):
    if (number % 8) == 0 and (number % 12) != 0:
        print(number)
    number += 1