def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer


a = [1, 1, 2, 3, 4, 5]
b = 1
result = solution(a,b)
print(result)
