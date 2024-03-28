def solution(ineq, eq, n, m):
    if ineq == "<":
        if eq == "=":
            return int(n <= m)
        else:
            return int(n < m)
    else:
        if eq == "=":
            return int(n >= m)
        else:
            return int(n > m)

# def solution(ineq, eq, n, m):
    # return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))


a = "<"
b = "="
c = 20
d = 50
# result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
result = solution(a, b, c, d)
print(result)

