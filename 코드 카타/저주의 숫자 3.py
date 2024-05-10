def find_prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


def solution(a, b):
    from fractions import Fraction
    answer = 2

    fraction = Fraction(a, b)
    try:
        a, b = str(fraction.limit_denominator()).split("/")
    except:
        return 1
    if list(set(find_prime_factors(int(b)))) in [[2], [5], [2, 5]]:
        answer -= 1

    return answer


a = 7
b = 20
# c = 20
# d = 50
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
# result = solution(a, b, c, d)
print(result)
