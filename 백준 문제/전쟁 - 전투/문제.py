import sys
# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
m, n = map(int, input().split())
people = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

white = 0
blue = 0


def make_team(x, y, color):
    count = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if people[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count


for i in range(n):
    for j in range(m):
        if people[i][j] == "W" and not visited[i][j]:
            white += make_team(i, j, "W") ** 2
        elif people[i][j] == "B" and not visited[i][j]:
            blue += make_team(i, j, "B") ** 2

print(white, blue)

# from collections import deque
#
#
# # 입장 좌표 및 색 들고 입장
# def bfs(x, y, color):
#     # 찾은 갯수
#     cnt = 1
#     # 큐 저장
#     queue = deque()
#     # 시작 지점 입력
#     queue.append((x, y))
#     # 시작지점 방문 완료
#     visited[x][y] = True
#
#     # 방문한 곳이 없을 때 까지 반복!
#     while queue:
#         # 방문 지점 하나 꺼내서 사용
#         x, y = queue.popleft()
#         # 좌표 이동 !
#         for i in range(4):
#             # 상하 이동
#             nx = x + dx[i]
#             # 좌우 이동
#             ny = y + dy[i]
#             # 범위 탈락
#             if 0 <= nx < m and 0 <= ny < n:
#                 # 이동한 곳이 내가 처음에 들고온 컬러랑 같은가?  그리고 방문한 적이 없는가?
#                 if graph[nx][ny] == color and not visited[nx][ny]:
#                     # 방문 완료
#                     visited[nx][ny] = True
#                     # 방문한 좌표 큐에 저장
#                     queue.append((nx, ny))
#                     # 사람수 추가
#                     cnt += 1  # each color count
#
#     return cnt
#
# # 좌표이동
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# # 칸 갯수
# n, m = map(int, input().split())
# # 군사 위치 표시
# graph = [list(input()) for _ in range(m)]
# # 방문 표시
# visited = [[False] * n for i in range(m)]
# # 흰 파 갯수
# white, blue = 0, 0
#
# for i in range(m):
#     for j in range(n):
#         # 흰색 이면서 방문 한 적이 없다면?
#         if graph[i][j] == 'W' and not visited[i][j]:
#             # i번째 j칸 컬러를 화이트로 들고 입장
#             white += bfs(i, j, 'W') ** 2  # count accumulate
#         elif graph[i][j] == 'B' and not visited[i][j]:
#             # i번째 j칸 컬러를 블루로 들고 입장
#             blue += bfs(i, j, 'B') ** 2  # count accumulate
#
# print(white, blue)






# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(input()))
#
# stack = []
# counter = 0
#
# print(graph)
#
#
# def W_check(x, y):
#     if 0 <= x < n and 0 <= y < m:
#         if graph[x][y] == "W" and (x, y) not in stack:
#             global counter
#             stack.append((x,y))
#             counter += 1
#             W_check(x + 1, y)
#             W_check(x, y + 1)
#             W_check(x - 1, y)
#             W_check(x, y - 1)
#
#
# def B_check(x, y):
#     if 0 <= x < n and 0 <= y < m:
#         if graph[x][y] == "B" and (x, y) not in stack:
#             global counter
#             stack.append((x,y))
#             counter += 1
#             W_check(x + 1, y)
#             W_check(x, y + 1)
#             W_check(x - 1, y)
#             W_check(x, y - 1)
#
# W_check(0, 0)
# print(counter)