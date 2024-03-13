import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

from collections import deque
# DFS용 실행 순서 리스트
list_dfs = []


# DFS 실행 함수
def dfs(graph_dfs, start, visited):
    # 처음 들어오는 구간에 방문 설정
    visited[start] = True
    # 리스트 전역 변수 설정
    global list_dfs
    # 실행 번호 리스트 추가
    list_dfs.append(start)
    # 실행 번호와 연결된 모든 번호 하나 씩 꺼내서 실행 (순서는 작은순 부터)
    for node in sorted(graph_dfs[start]):
        # 방문 한적이 없으면 실행
        if not visited[node]:
            dfs(graph_dfs, node, visited)


# BFS 실행 함수
def bfs(graph_bfs, start, node):
    # 방문 여부 리스트 만들기
    visited_bfs = [False] * (node + 1)
    # 큐를 만들어서 순서대로 실행 할 수 있도록
    queue = deque()
    # 현재 함수 시작할 때 번호 큐 추가
    queue.append(start)
    # 방문 설정 추가
    visited_bfs[start] = True
    # BFS리스트 생성
    list_bfs = []
    while queue:
        # 큐에 있는 번호 꺼내서 넣기
        vertex = queue.popleft()
        # 큐에서 꺼낸 번호 리스트에 추가
        list_bfs.append(vertex)
        # 큐에 꺼낸 번호에 연결된 번호 전부 검사
        for neighbour in sorted(graph_bfs[vertex]):
            # 방문한 적이 없다면 큐리스트에 추가
            if not visited_bfs[neighbour]:
                # 큐에 추가하고 방문 체크 하기
                queue.append(neighbour)
                visited_bfs[neighbour] = True
    # 번호 리스트 값 리턴
    return list_bfs


# 노드 갯수, 연결 횟수, 시작 번호 입력
n, m, v = map(int, input().split())
# 각 노드에 연결된 번호 그래프 출력 0번은 필요 없는 번호
graph = [[] for _ in range(n + 1)]
# 각 연결마다 노드 추가 하기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS에 필요한 방문 표기 만들어주기
visited_dfs = [False] * (n + 1)

# DFS입장
dfs(graph, v, visited_dfs)
# 리스트 출력
print(*list_dfs)
# BFS입장 후 결과 출력
print(*bfs(graph, v, n))
