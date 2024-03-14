import sys

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def power(a, b, c):
    if b == 0:
        return 1

    x = power(a, b // 2, c)

    if b % 2 == 0:
        return (x * x) % c

    else:
        return (x * x * a) % c


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    a, b, k = map(int, input().split())

    c = a + b

    a = (a * power(2, k, c)) % c

    b = c - a

    print(f"#{test_case} {min(a, b)}")

# --------- 튜터님 기회!-------
# def division(n, _sum):
#     if n == 0:
#         return 1
#     result = division(n // 2, _sum)
#     result = (result * result) % _sum
#     if n % 2 == 1:
#         result = (result * 2) % _sum
#     return result
#
#
# def find(a, b, k):
#     _sum = a + b
#     result = (division(k, _sum) * a) % _sum
#     return min(result, _sum - result)
#
#
# if __name__ == "__main__":
#     t = int(input())
#     for i in range(t):
#         a, b, k = map(int, input().split())
#         print("#{} {}".format(i + 1, find(a, b, k)))


# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#
#     a, b, k = map(int, input().split())
#
#     c = a + b
#
#     a = (a * (2 ** k)) % c
#
#     b = c - a
#
#     print(f"#{test_case} {min(a, b)}")




    # -----시간 초과!-------
    # a, b, k = map(int, input().split())
    #
    # for _ in range(k):
    #     if a <= b:
    #         c = a
    #         a *= 2
    #         b -= c
    #     else:
    #         c = b
    #         b *= 2
    #         a -= c
    #
    # print(f"#{test_case} {min(a, b)}")