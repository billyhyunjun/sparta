import sys
from collections import deque

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

# 칸수 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# m이 y의 갯수 n이 x의 갯수다!
m, n = map(int, input().split())
# n의 단어가 m줄 있습니다.
maze = [list(map(int, input())) for _ in range(m)]
# 큐 생성 = 탐험해야 할 목록
queue = deque()

# ----- 미로 확인 용 궁금 하면 주석 풀고 확인 ----
# for i in maze:
#     print(i)
# 0,0 부터 시작
queue.append((0, 0))
# 탐험 시작
while queue:
    # 탐험 목록에서 가장 먼저 해야 할 것 꺼내기
    x, y = queue.popleft()
    # 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안이면서 값이 1인 땅 찾기
        if 0 <= nx < n and 0 <= ny < m and maze[ny][nx] == 1:
            # 탐험 목록 추가
            queue.append((nx, ny))
            # 지금 위치에 전의 값보다 1 많게 해서 값 변경
            maze[ny][nx] = maze[y][x] + 1
# 최종 목적지의 값
print(maze[m - 1][n - 1])
