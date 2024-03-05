def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer


a = [1, 2, 3, 4, 5]
b = 1
c = 3
result = solution(a,b,c)
print(result)
