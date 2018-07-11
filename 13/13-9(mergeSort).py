# 두 리스트 합치기
def merge(list1, list2):
    # 코드를 입력하세요.
    new_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

    # list1에 남은 원소가 있다면, new_list에 추가하기
    # 코드를 작성하세요.
    for a in range(i,len(list1)):
        new_list.append(list1[a])

    # list2에 남은 원소가 있다면, new_list에 추가하기
    # 코드를 작성하세요.
    for b in range(j,len(list2)):
        new_list.append(list2[b])

    return new_list

# 합병 정렬
def merge_sort(my_list):
    # Base Case
    # 코드를 작성하세요.
    if(len(my_list) < 2):
        return my_list

    # Recursive Case: left와 right로 my_list를 나누어준다.
    left = my_list[:len(my_list) // 2]
    right = my_list[len(my_list) // 2:]

    # Recursive Case: my_list를 잘게 쪼개는 과정을 재귀적으로 반복하고, merge 함수를 사용하여 합쳐준다.
    # 코드를 작성하세요.
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)


some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)