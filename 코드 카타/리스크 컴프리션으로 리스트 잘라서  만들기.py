def solution(num_list, n):
    answer = []
    [answer.append(item) for item in num_list[n:]]
    [answer.append(item) for item in num_list[:n]]
    return answer


a = [2, 1, 6]
b = 1
# c = 3
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
print(result)