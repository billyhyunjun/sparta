def solution(a, b, flag):
    if flag:
        answer = a + b
    else:
        answer = a - b
    return answer


a = -4
b = 7
c = True
result = solution(a, b, c)
print(result)
