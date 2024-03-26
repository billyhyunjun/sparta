def solution(arr):
    try:
        find_2 = arr.index(2)
        reverse_list = arr[::-1]
        find_2_reverse = len(arr) - reverse_list.index(2) - 1
    except ValueError:
        return [-1]
    return arr[find_2 : find_2_reverse + 1]

# def solution(arr):
#     if 2 not in arr:
#         return [-1]
#     return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]


a = [1, 1, 1]
# b = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]
# c = True
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)