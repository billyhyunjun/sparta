from collections import deque


def solution(n, edge):
    # 그래프 생성
    graph = [[] for _ in range(n+1)]
    # 노드거리
    distance = [0 for _ in range(n+1)]
    # 그래프 엮기
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    # 큐생성
    queue = deque()
    # 큐의 1번 노드 넣기
    queue.append(1)
    # 1번 노드는 거리 1
    distance[1] = 1
    # 반복문 진행
    while queue:
        # 큐에서 꺼내기
        node = queue.popleft()
        # 노드와 연결된 모든 노드 반복
        for neighbor in graph[node]:
            # 방문한 적 없으면 큐에 넣고 전 노드 위치 값에 1 더하기
            if not distance[neighbor]:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    # 최고 거리 값 출력
    return distance.count(max(distance))


a = 6
b = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# c = 3
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
print(result)
