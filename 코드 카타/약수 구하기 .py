def solution(a, b, c):
    if a == b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a != b and b != c and c != a:
        answer = (a + b + c)
    else:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    return answer


a = 3
b = 5
c = 3
# result = solution(a)
# result = solution(a, b)
result = solution(a, b, c)
print(result)
