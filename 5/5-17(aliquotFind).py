n = 120
i = 1
num = 0
while (i <= 120):
    if (n % i) == 0:
        print(i)
        num += 1
    i += 1
print("%d의 약수는 총 %d개입니다." %(n, num))