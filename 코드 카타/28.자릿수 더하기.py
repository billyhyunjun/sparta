def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer


a = 1234
# b = 12
# c = 3
result = solution(a)
print(result)
