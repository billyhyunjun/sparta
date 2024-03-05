def solution(sides):
    triangle = sorted(sides)
    if  triangle[-1] < triangle[0] + triangle[1]:
        answer = 1
    else:
        answer = 2
    return answer


a = [1, 2, 3]
# b = 10
# c = 3
result = solution(a)
print(result)
