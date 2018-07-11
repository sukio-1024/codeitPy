from random import randint

ANSWER = randint(1,20)
tries = 0
while (tries < 4):
    guess = int (input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " %(4 - tries)))
    if (guess == ANSWER):
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." %(tries + 1))
        break
    elif (guess > ANSWER):
        print("Down")
    else:
        print("Up")
    tries += 1
if (tries == 4) and (guess != ANSWER):
    print("아쉽습니다. 정답은 %d였습니다." %(ANSWER))