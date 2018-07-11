# 선택 정렬

def selection_sort(my_list):
    # 코드를 입력하세요.
    for i in range(len(my_list)):
        smallest = i
        for j in range(i + 1, len(my_list)):
            value = my_list[j]
            if value < my_list[smallest]:
                smallest = j
        temp = my_list[i]
        my_list[i] = my_list[smallest]
        my_list[smallest] = temp


some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)