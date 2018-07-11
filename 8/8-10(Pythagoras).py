for a in range(1, 333):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        # 코드를 작성하세요.
        if (c ** 2) == ((a ** 2) + (b ** 2)) and (a < b < c):
            print(a * b * c)