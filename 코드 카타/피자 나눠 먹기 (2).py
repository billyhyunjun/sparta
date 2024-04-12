def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        sum_num = 0
        while sum_num < n:
            sum_num += i
            if sum_num == n:
                answer += 1
                break
            i += 1
    return answer


a = 15
# b = 9
# c = 2
# d = 50
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
