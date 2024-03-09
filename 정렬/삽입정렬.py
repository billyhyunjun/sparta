# 선택정렬을 만들어 보자!
def insertion_sort(array):
    for end in range(1, len(array)):
        for i in range(end, 0, -1):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
    return array

# 엉망 진창 리스트!
list = [1, 5, 4, 8, 6, 2, 7, 3, 9]
# 함수 호출!
sorted_list = insertion_sort(list)

print(sorted_list)
