def solution(n):
    integer_square_root = int(n ** 0.5)

    if integer_square_root ** 2 == n:
        answer = 1
    else:
        answer = 2
    return answer

a = 144
# b = 3
# c = 3
result = solution(a)
print(result)
