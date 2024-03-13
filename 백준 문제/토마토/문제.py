import sys
from collections import deque

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

# 상하좌우 이동 방법
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

m, n = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(n)]

queue = deque()


for y in range(n):
    for x in range(m):
        if tomato[y][x] == 1:
            queue.append((x, y))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and tomato[ny][nx] == 0:
            tomato[ny][nx] = tomato[y][x] + 1
            queue.append((nx, ny))

flag = True
max_day = 0

for i in tomato:
    if 0 in i:
        print(-1)
        flag = False
        break
    else:
        if max_day < max(i):
            max_day = max(i)

if flag:
    print(max_day - 1)