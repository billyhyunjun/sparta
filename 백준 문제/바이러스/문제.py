import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

computers = int(input())
links = int(input())
# 0번 때문에 컴퓨터 보다 하나 많게
graph = [[] for _ in range(computers + 1)]
# 감염 유무
infected = [0 for _ in range(computers + 1)]

for i in range(links):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
# 1번 컴퓨터 감염
infected[1] = 1


# 감염 시키자
def virus(com_num):
    # 당신의 컴퓨터는 감염 되었습니다
    infected[com_num] = 1
    # 그러면 당신과 연결되어 있는 켬퓨터가 누구인지 볼까요?
    for linked_com in graph[com_num]:
        # 그 목록중에 감염이 되어 있지 않은 컴퓨터가 있나요?
        if infected[linked_com] == 0:
            # 감염되지 않은 컴퓨터로 들어갑니다.
            virus(linked_com)


# 1번 컴퓨터 부터 시작
virus(1)
# 1번이 감염 시킨 컴퓨터 니깐 1번을 빼서 -1
print(sum(infected) - 1)




# ---- 다른 방법 ----
# from collections import deque
# n=int(input()) # 컴퓨터 개수
# v=int(input()) # 연결선 개수
# graph = [[] for i in range(n+1)] # 그래프 초기화
# visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
# for i in range(v): # 그래프 생성
#     a,b=map(int,input().split())
#     graph[a]+=[b] # a에 b 연결
#     graph[b]+=[a] # b에 a 연결 -> 양방향
# visited[1]=1 # 1번 컴퓨터부터 시작이니 방문 표시
# Q=deque([1])
# while Q:
#     c=Q.popleft()
#     for nx in graph[c]:
#         if visited[nx]==0:
#             Q.append(nx)
#             visited[nx]=1
# print(sum(visited)-1)


# ---- 해답 ----
#
# n = int(input())  # 컴퓨터 개수
# v = int(input())  # 연결선 개수
# # graph : [[], [], [], [], [], [], [], []] 각 위치별로 [com0(필요없음), com1, com2, com3,.... com7]
# graph = [[] for i in range(n + 1)]  # 그래프 초기화
# # visited : [0, 0, 0, 0, 0, 0, 0, 0] 감염상태
# visited = [0] * (n + 1)  # 방문한 컴퓨터인지 표시
# for i in range(v):  # 그래프 생성
#     a, b = map(int, input().split())
#     graph[a] += [b]  # a에 b 연결
#     graph[b] += [a]  # b에 a 연결 -> 양방향
#
#
# def virus(v):
#     visited[v] = 1
#     for infection in graph[v]:
#         if visited[infection] == 0:
#             virus(infection)
#
#
# virus(1)
# print(sum(visited) - 1)
#

# ----- 처음에 만든거 ----

# num = int(input())
# link = int(input())
# linked_list = []
# for i in range(link):
#     linked_list.append(set(map(int, input().split())))
#
# def virus(idx, virus_list):
#     if idx == link:
#         print(len(virus_list) - 1)
#         return
#     if len(virus_list | linked_list[idx]) != len(virus_list) + len(linked_list[idx]):
#         new_list = virus_list | linked_list[idx]
#         virus(idx + 1, new_list)
#     else:
#         virus(idx + 1, virus_list)
#
#
# for i, l in enumerate(linked_list):
#     if 1 in l:
#         virus(0, linked_list[i])
#         break
