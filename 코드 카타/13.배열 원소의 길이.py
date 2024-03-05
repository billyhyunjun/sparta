def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer


a = ["We", "are", "the", "world!"]

result = solution(a)
print(result)
