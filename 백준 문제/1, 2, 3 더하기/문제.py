import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def solution(n):
    if n < 4:
        if n < 3:
            return n
        else:
            return 4
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    return d[n]


# 테스트 반복 !
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = int(input())
    result = solution(a)
    print(result)
