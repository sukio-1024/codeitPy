# 자리수 합 리턴

def sum_digit(num):
    sum = 0
    numString = str(num)
    i = 0
    while (i < len(numString)):
        sum += int(numString[i])
        i += 1
    return sum

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
resultSum = 0
for num in range(1,1001):
    resultSum += sum_digit(num)

print(resultSum)