def solution(my_string, s, e):
    answer = ''
    for i in range(0, s):
        answer += my_string[i]
    for i in range(e, s-1, -1):
        answer += my_string[i]
    for i in range(e+1,len(my_string)):
        answer += my_string[i]
    return answer
def solution(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]


a = "Progra21Sremm3"
b = 6
c = 12
# result = solution(a)
# result = solution(a, b)
result = solution(a, b, c)
print(result)