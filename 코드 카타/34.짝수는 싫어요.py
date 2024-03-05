def solution(n):
    answer = []
    for i in range(1,n+1):
        if i % 2 != 0:
            answer.append(i)
        else:
            pass
    return answer


a = 10
# b = 10
# c = 3
result = solution(a)
print(result)
