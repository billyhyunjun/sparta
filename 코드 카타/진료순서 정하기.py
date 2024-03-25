def solution(emergency):
    answer = []
    top = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(top.index(i)+1)
    return answer


a = [3, 76, 24]
# b = 20
# c = True
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
