def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer

a = "hello"
b = 3
# c = 3
result = solution(a, b)
print(result)
