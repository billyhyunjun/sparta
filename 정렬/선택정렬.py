# 선택정렬을 만들어 보자!
def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        min_value = array[i]
        for j in range(i + 1, len(array)):
            if min_value > array[j]:
                min_index = j
                min_value = array[j]
        array[i], array[min_index] = array[min_index], array[i]
    return array

# 또 다른 버전
# def selection_sort(array):
#     for i in range(len(array)-1):
#         for j in range(i + 1, len(array)):
#             if array[i] > array[j]:
#                 array[i], array[j] = array[j], array[i]
#     return array

# 엉망 진창 리스트!
list = [1, 5, 4, 8, 6, 2, 7, 3, 9]
# 함수 호출!
sorted_list = selection_sort(list)

print(sorted_list)
