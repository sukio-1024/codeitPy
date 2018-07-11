# 삽입 정렬
def insertion_sort(my_list):
    # 코드를 입력하세요.
    for i in range(len(my_list)):
        key = my_list[i]
        keyCode = i
        for j in range(1,i+1):
            if(i > 0) and (my_list[i-j] > key):
                my_list[i-j+1] = my_list[i-j]
                keyCode = i-j
        my_list[keyCode] = key

some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)