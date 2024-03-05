def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer


a = [149, 180, 192, 170]
b = 167

result = solution(a, b)
print(result)
