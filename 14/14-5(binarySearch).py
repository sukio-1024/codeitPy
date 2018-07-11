def binary_search(element, some_list):
    # 코드를 작성하세요.
    start_index = 0
    end_index = len(some_list) - 1
    while (start_index <= end_index):
        mid_index = (end_index + start_index) // 2
        if(some_list[mid_index] == element):
            return mid_index
        elif(some_list[mid_index] < element):
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11])) # 0
print(binary_search(0, [2, 3, 5, 7, 11])) # None
print(binary_search(5, [2, 3, 5, 7, 11])) # 2
print(binary_search(3, [2, 3, 5, 7, 11])) # err
print(binary_search(11, [2, 3, 5, 7, 11]))