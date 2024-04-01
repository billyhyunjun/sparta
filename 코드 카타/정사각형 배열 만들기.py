def solution(arr):
    if len(arr) > len(arr[-1]):
        for i in range(len(arr)):
            for j in range(len(arr) - len(arr[-1])):
                arr[i].append(0)
    elif len(arr) < len(arr[-1]):
        for i in range(len(arr[-1])):
            for j in range(len(arr[-1]) - len(arr)):
                arr.append([0] * len(arr[-1]))
    return arr

# def solution(arr):
#     num_rows = len(arr)
#     num_cols = len(arr[0])
#
#     if num_rows > num_cols:
#         for i in range(num_rows):
#             arr[i] += [0] * (num_rows - num_cols)
#     elif num_cols > num_rows:
#         for i in range(num_cols - num_rows):
#             arr.append([0] * num_cols)
#
#     return arr


a = [[57, 192, 534, 2], [9, 345, 192, 999]]
# b = 3
# c = 20
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
