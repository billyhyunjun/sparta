# def solution(a, b):
#     answer = 0
#     for i in range(len(a)):
#         answer += a[i] * b[i]
#     return answer

def solution(a, b, c):
    return [x*y*z for x, y, z in zip(a,b,c)]

a = [1,2,3,4,5]
b = [-3,-1,0]
c = [-3,-1,0,2,4]
# d = True
# result = solution(a)
result = solution(a, b, c)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)