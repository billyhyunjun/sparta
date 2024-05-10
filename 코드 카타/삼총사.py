from itertools import combinations


def solution(number):
    answer = 0
    num_list = list(combinations(number, 3))
    for i in num_list:
        if sum(i) == 0:
            answer += 1
    return answer


a = [-3, -2, -1, 0, 1, 2, 3]
# b = [[1,2]]
# c = 20
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
