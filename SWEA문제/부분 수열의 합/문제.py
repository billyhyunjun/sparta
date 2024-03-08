import sys
from itertools import combinations

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def match_line(value, num_list):
    global counter
    remove_list = [x for x in num_list if x <= value]
    for i in range(1, len(remove_list) + 1):
        num = combinations(remove_list, i)
        for j in num:
            if sum(j) == value:
                counter += 1


T = int(input())
# 여러 개의 테스트 케이스 가 주어 지므로, 각각을 처리 합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    list_map = []
    numbers = list(map(int, input().split()))
    counter = 0

    match_line(k, numbers)

    print(f"#{test_case} {counter}")
