def solution(numbers):
    list = sorted(numbers, reverse=True)
    answer = list[0] * list[1]
    return answer


a = [1, 2, 3, 4, 5]
# b = "f"
# c = 3
result = solution(a)
print(result)
