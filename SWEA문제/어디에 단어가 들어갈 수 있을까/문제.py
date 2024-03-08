import sys

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def match_line(num, line):
    global counter
    for char in line:
        block = 0
        for index, x in enumerate(char, 1):
            if x == 1:
                block += 1
            else:
                if block == num:
                    counter += 1
                    block = 0
                else:
                    block = 0
            if index == len(char) and block == num:
                counter += 1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    counter = 0

    n, k = map(int, input().split())
    list_map = []
    for i in range(n):
        list_map.append(list(map(int, input().split())))

    # 빈곳 검사
    match_line(k, list_map)
    # 행렬 변환
    list_map = list(map(list, zip(*list_map)))
    # 빈곳 검사
    match_line(k, list_map)

    print(f"#{test_case} {counter}")
