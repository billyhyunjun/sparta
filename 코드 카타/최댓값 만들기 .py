from functools import reduce
from itertools import combinations


def solution(numbers):
    answer = -float("inf")
    perm = list(combinations(numbers, 2))
    for i in perm:
        multi = reduce(lambda x, y: x * y, i)
        if multi > answer:
            answer = multi
    return answer


a = [1, 2, -3, 4, -5]
# b = 1
# c = 3
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
print(result)
