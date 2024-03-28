def solution(my_string, queries):
    for i, j in queries:
        my_string = my_string[:i] + my_string[i:j+1][::-1] + my_string[j+1:]
    return my_string


a = '12121212'
b = [[1,2]]
# c = 20
# d = 50
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
# print(a[3:1:-1])