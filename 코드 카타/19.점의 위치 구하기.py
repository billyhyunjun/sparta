def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            answer = 1
        else:
            answer = 4
    else:
        if dot[1] > 0:
            answer = 2
        else:
            answer = 3
    return answer


a = [7, -9]
# b = 1
# c = 3
result = solution(a)
print(result)
