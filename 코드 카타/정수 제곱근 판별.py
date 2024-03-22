import math


def solution(n):
    square_root = math.sqrt(n)
    if square_root == int(square_root):
        return (round(square_root) + 1)**2
    return -1


a = 121
# b = 5
# # c = 3
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
print(result)