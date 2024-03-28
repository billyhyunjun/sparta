def solution(my_string):
    answer = [0]*52
    for char in my_string:
        if char.isupper():
            answer[ord(char) - 65] += 1
        elif char.islower():
            answer[ord(char) - 71] += 1
    return answer

# print(["Programmers".count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz'])

a = "Programmers"
# b = 20
# c = 4
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)

