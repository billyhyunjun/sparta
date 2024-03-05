def solution(my_string):
    vowel = ["a", "e", "i", "o", "u"]
    answer = ''
    for i in my_string:
        if i in vowel:
            pass
        else:
            answer += i
    return answer

a = "bus"
# b = 10
# c = 3
result = solution(a)
print(result)
