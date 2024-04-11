def solution(n):
    ternary = ""

    while n > 0:
        remainder = n % 3
        ternary = str(remainder) + ternary
        n = n // 3

    x = 1
    answer = 0
    for i in ternary:
        answer += int(i) * x
        x *= 3

    return answer

# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3
#
#     answer = int(tmp, 3)
#     return answer


a = 45
# b = [7, 9]
# c = 2
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
