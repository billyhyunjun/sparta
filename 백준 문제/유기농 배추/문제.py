import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

# 상하좌우 이동 방법
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 테스트 횟수
T = int(input())
# 테스트 횟수에 맞추어 반복 시작
for _ in range(T):

    m, n, k = map(int, input().split())

    matrix = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1

    counter = 0

    def solution(y, x):
        stack = [(y, x)]
        matrix[y][x] = 0
        while stack:
            y, x = stack.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n and matrix[ny][nx] == 1:
                    matrix[ny][nx] = 0
                    stack.append((ny, nx))


    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                counter += 1
                solution(i, j)

    print(counter)


# ---재귀------
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
#
# T = int(input())
# for _ in range(T):
#
#     m, n, k = map(int, input().split())
#
#     matrix = [[0 for _ in range(m)] for _ in range(n)]
#
#     for _ in range(k):
#         a, b = map(int, input().split())
#         matrix[b][a] = 1
#
#
#     counter = 0
#
#     def solution(y, x):
#         matrix[y][x] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < m and 0 <= ny < n and matrix[ny][nx] == 1:
#                 solution(ny, nx)
#
#
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 1:
#                 counter += 1
#                 solution(i, j)
#
#     print(counter)