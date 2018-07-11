from random import randint

numbers = [] # 랜덤한 뽑기 숫자
userNumber = [] # 사용자가 입력한 숫자
number = 0 # 몇번만에 맞췄는지를 세기 위한 변수

# 세개 뽑을때까지 반복
while len(numbers) < 3:
    new_number = randint(0, 9)

    # 새로운 수 나올때까지 다시 뽑기
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

i = 0
sports = True
strike = 0 # S
ball = 0 # B
while(sports):
    print("세 수를 하나씩 차례대로 입력하세요.")
    while(i < 3):
        inputNum = int(input("%d번째 수를 입력하세요: " % (i + 1)))
        if (inputNum >= 0) and (inputNum < 10):
            if (inputNum in userNumber):
                print("중복되는 수입니다. 다시 입력해주세요.")
            else:
                userNumber.append(inputNum)
                i += 1
        else:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
    a = 0
    while (a < 3):
        if (userNumber[a] == numbers[a]):
            strike += 1
        elif (userNumber[a] in numbers):
            ball += 1
        a += 1

    print("%dS %dB" %(strike, ball))

    if (strike == 3):
        print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (number))
        break
    else:
        strike = 0
        ball = 0
        i = 0
        number += 1
        del userNumber[0:]
