def solution(number, n, m):
    if number % n == 0 and number & m == 0:
        return 1
    return 0


a = 60
b = 2
c = 3
result = solution(a, b, c)
print(result)