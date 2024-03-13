import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

from collections import deque

# 컴퓨터 및 연결 수 입력
computers = int(input())
links = int(input())
# 검사 목록 명단
queue = deque()
# 그래프를 이용 각 컴퓨터 번호에 연결 되어 있는 컴퓨터를 표시
linked_com = [[] for _ in range(computers)]
# 컴퓨터가 감염이 되어 있는지 확인 유무
infection = [0 for _ in range(computers)]

# 연결에 맞추어 각 컴퓨터에 연결 번호를 입력
for i in range(links):
    a, b = map(int, input().split())

    linked_com[a - 1].append(b - 1)
    linked_com[b - 1].append(a - 1)

# 1번 컴퓨터 즉 0번 위치에 있는 컴퓨터를 감염시키고 검사목록에 올려 놓기
infection[0] = 1
queue.append(0)

# 더이상 검사를 할게 없을 때까지 반복하기
while len(queue) > 0:
    # 검사 목록에서 하나 빼서 그 컴퓨터와 연결 되어 있는 것들 다 가져오기
    com = queue.popleft()
    # 연결 된 컴퓨터가 감염이 되어 있는지????
    for i in linked_com[com]:
        # 감염이 안되어 있는 컴퓨터라면 감염을 시키고 그 컴퓨터랑 연결 되어 있는 컴퓨터를 전부 검사 목록으로 넣는다.
        if infection[i] == 0:
            infection[i] = 1
            queue.append(i)

# 1번 컴퓨터가 감염시킨 컴퓨터 수 이므로 1번은 빼준다.
print(sum(infection) - 1)

# n = int(input())  # 컴퓨터 개수
# v = int(input())  # 연결선 개수
#
# graph = [[] for i in range(n + 1)]  # 그래프 초기화
#
# visited = [0] * (n + 1)  # 방문한 컴퓨터인지 표시
#
# for i in range(v):  # 그래프 생성
#
#     a, b = map(int, input().split())
#
#     graph[a] += [b]  # a에 b 연결
#
#     graph[b] += [a]  # b에 a 연결 -> 양방향
#
# visited[1] = 1  # 1번 컴퓨터부터 시작이니 방문 표시
#
# Q = deque([1])
#
# while Q:
#
#     c = Q.popleft()
#
#     for nx in graph[c]:
#
#         if visited[nx] == 0:
#             Q.append(nx)
#
#             visited[nx] = 1
#
# print(sum(visited) - 1)
