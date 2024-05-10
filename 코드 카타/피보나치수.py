def solution(n):
    answer = 0

    if n < 2:
        return n
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[n] % 1234567


a = 3
# b = [[1,2]]
# c = 20
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
