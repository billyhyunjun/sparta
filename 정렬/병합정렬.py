# 선택정렬을 만들어 보자!
def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    low_array = merge_sort(array[:mid])
    high_array = merge_sort(array[mid:])

    merged_array = []
    l = h = 0
    while l < len(low_array) and h < len(high_array):
        if low_array[l] < high_array[h]:
            merged_array.append(low_array[l])
            l += 1
        else:
            merged_array.append(high_array[h])
            h += 1
    merged_array += low_array[l:]
    merged_array += high_array[h:]
    return merged_array

# 엉망 진창 리스트!
list = [1, 5, 4, 8, 6, 2, 7, 3, 9]
# 함수 호출!
sorted_list = merge_sort(list)

print(sorted_list)
