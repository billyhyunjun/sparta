# 선택정렬을 만들어 보자!
def selection_sort(array):
    length = len(array)
    for i in range(length-1):
        min_index = i
        for j in range(i + 1, length):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# # 또 다른 버전
# def selection_sort(array):
#     for i in range(len(array)-1):
#         for j in range(i + 1, len(array)):
#             if array[i] > array[j]:
#                 array[i], array[j] = array[j], array[i]
#     return array

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# Select = [5, 3, 8, 4, 2]
# print("정렬전 리스트:", Select)
# Selectsort = []
#
# for i in range(len(Select)):
#     min_index = Select.index(min(Select))
#     min_value = Select.pop(min_index)
#     Selectsort.append(min_value)
#
# print("정렬된 리스트:", Selectsort)

# 엉망 진창 리스트!
list = [1, 5, 4, 8, 6, 2, 7, 3, 9]
# 함수 호출!
sorted_list = selection_sort(list)

print(sorted_list)
