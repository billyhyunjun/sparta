def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if letter == i:
            pass
        else:
            answer += i
    return answer


a = "abcdef"
b = "f"
# c = 3
result = solution(a, b)
print(result)
