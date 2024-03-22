def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a + (d * i)
    return answer


a = 3
b = 4
c = [True, False, False, True, True]
# result = solution(a)
# result = solution(a, b)
result = solution(a, b, c)
print(result)