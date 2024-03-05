def solution(my_string, n):
    answer = ''
    for i in range(n):
        answer += my_string[i]
    return answer

# def solution(my_string, n):
#     answer = my_string[:n]
#     return answer

a = "ProgrammerS123"
b = 11
# c = 3
result = solution(a, b)
print(result)
