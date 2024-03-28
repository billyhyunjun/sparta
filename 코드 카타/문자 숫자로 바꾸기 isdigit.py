def solution(s):
    if len(s) == 6 or len(s) == 4:
        try:
            c = int(s)
            return True
        except ValueError:
            return False
    else:
        return False


# def alpha_string46(s):
#     return s.isdigit() and len(s) in [4, 6]


a = "a234"
# b = 5
# c = 4
# d = True
result = solution(a)
# result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
print(len(23))

