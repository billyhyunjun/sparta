import sys

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def power(n, m):
    if m == 1:
        return n
    else:
        n *= power(n, m - 1)

    return n


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    n, m = map(int, input().split())

    print(f"#{num} {power(n, m)}")
