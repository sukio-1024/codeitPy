from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    # 코드를 입력하세요
    numbers = []
    while (len(numbers) < 6):
        number = randint(1, 45)
        if number not in numbers:
            numbers.append(number)

    numbers.sort()
    return numbers

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    # 코드를 입력하세요
    win_num_list = generate_numbers()
    Bnumber = randint(1,45)

    while(Bnumber in win_num_list):
        Bnumber = randint(1,45)

    win_num_list.append(Bnumber)

    return win_num_list


# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    # 코드를 입력하세요
    count = 0
    for i in range(0,6):
        if(list1[i] in list2):
            count += 1
    return count


# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # 코드를 입력하세요
    countNum = count_matching_numbers(numbers, winning_numbers[:6])
    if(winning_numbers[len(winning_numbers)-1] not in numbers):
        if(countNum == 6):
            return 1000000000
        elif(countNum == 5):
            return 1000000
        elif(countNum == 4):
            return 50000
        elif (countNum == 3):
            return 5000
    else :
        if(countNum == 6):
            return 50000000
        else :
            return 0
