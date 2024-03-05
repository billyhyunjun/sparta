def solution(str1, str2):
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer


a = "ppprrrogrammers"
b = "pppp"
# c = 3
result = solution(a, b)
print(result)
