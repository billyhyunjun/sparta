def solution(n):
    answer = 0
    bytes = bin(n)[2:]
    count = bytes.count("1")
    while True:
        n += 1
        answer = bin(n)[2:]
        if answer.count("1") == count:
            break
    return n


a = 78
# b = [[1,2]]
# c = 20
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
