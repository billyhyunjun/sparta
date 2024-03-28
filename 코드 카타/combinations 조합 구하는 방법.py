import math


def solution(balls, share):
    return math.comb(balls, share)

#
# def solution(balls, share):
#     mul = 1
#     for i in set(range(1, balls + 1))-set(range(1, share + 1)):
#         mul *= i
#     for i in range(balls-share, 0,-1):
#         mul//= i
#     return mul


a = 3
b = 2
# c = 20
# d = 50
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
