import heapq  # heapq 모듈 - 우선순위 큐 기능 사용


def dijkstra(graph, start):
    # 무한대를 저장하기 위해 float 자료형, 초기화 진행
    distances = {vertex: float('infinity') for vertex in graph}
    # 시작 정점의 최단 거리 0으로 설정함
    distances[start] = 0
    # 우선순위 큐 초기화. (거리, 정점) 튜플
    priority_queue = [(start, 0)]

    # 우선순위 큐가 비어있지 않는 동안 반복
    while priority_queue:
        # 우선순위 큐에서 최단 거리 정점을 추출
        current_vertex, current_distance = heapq.heappop(priority_queue)
        # 추출된 정점의 거리가 이미 알고 있는 거리보다 크면 무시
        if current_distance > distances[current_vertex]:
            continue

        # 현재 정점 모든 이웃을 순회
        for neighbor, weight in graph[current_vertex].items():
            # 현재 정점을 지나 이웃에 도달하는 거리를 계산
            distance = current_distance + weight
            # 거리가 기존에 알려진 이웃의 최단 거리보다 작으면 갱신(update)
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # 업데이트된 거리와 이웃 정점을 우선순위 큐에 추가
                heapq.heappush(priority_queue, (neighbor, distance))

    # 모든 정점의 최단 거리를 담은 딕셔너리(테이블)를 반환
    return distances


# 각 도시를 정점으로 하고 도시 간 거리를 가중치로 한 그래프를 정의(입력 값 대신)
graph = {
    "Seoul": {"Wonju": 88, "Daejeon": 140, "Gwangju": 270, "Sokcho": 168},
    "Wonju": {"Seoul": 88, "Sokcho": 110, "Daejeon": 120, "Busan": 260},
    "Daejeon": {"Wonju": 120, "Seoul": 140, "Gwangju": 200, "Busan": 200},
    "Gwangju": {"Daejeon": 200, "Seoul": 270, "Busan": 200},
    "Busan": {"Gwangju": 200, "Daejeon": 200, "Wonju": 200, "Sokcho": 340},
    "Sokcho": {"Seoul": 168, "Wonju": 110, "Busan": 340},
}

distances_from_seoul = dijkstra(graph, "Seoul")

print(distances_from_seoul)
