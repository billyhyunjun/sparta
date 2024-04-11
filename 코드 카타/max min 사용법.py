def solution(dots):
    answer = sorted(dots, key=lambda x: x[1])
    return abs(answer[0][0] - answer[1][0]) * abs(answer[1][1] - answer[2][1])

# def solution(dots):
#     return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])


a = [[1, 1], [2, 1], [2, 2], [1, 2]]
# b = [7, 9]
# c = 2
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
