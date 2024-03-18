from collections import deque


def solve(city):
    # 최단거리 표
    distance = {}
    # 방문 여부
    visited = {}
    # 표 내용 채워주기
    for i in city:
        # 일단 최단거리를 구해야 하니 기본 값은 무한대
        distance[i] = float("inf")
        # 방문자 표시 0은 아직 1은 방문완료
        visited[i] = 0
    # 큐생성
    queue = deque()
    # 시작 지점은 거리 0
    distance[start] = 0
    # 시작 지점 큐에 넣기
    queue.append(start)
    # 반복문 지역 탐색 시작
    while len(queue):
        # 현재 위치
        current = queue.popleft()
        # 방문 여부
        if not visited[current]:
            # 방문한 적이 없으면 방문 1
            visited[current] = 1
            # 방문한 구간에서 각 이웃지역 거리
            for neighbor, weight in city[current].items():
                # 지존 도착 지역 이랑 자기 지역에 가는 거리 합친 것 대소 비교
                if distance[neighbor] > distance[current] + weight:
                    # 계산 값이 작다면 값 변경
                    distance[neighbor] = distance[current] + weight
                # 큐에 명단 넣기
                queue.append(neighbor)
    # 도착지의 거리 리턴
    return distance[end]


while True:
    start = input("시작 지점 지역명 \n(Seoul,Wonju,Daejeon,Gwangju,Busan,Sokcho)\n 입력:")
    end = input("종료 지점 지역명 \n(Seoul,Wonju,Daejeon,Gwangju,Busan,Sokcho)\n 입력 :")
    if (start in ["Seoul", "Wonju", "Daejeon", "Gwangju", "Busan", "Sokcho"] and
            end in ["Seoul", "Wonju", "Daejeon","Gwangju", "Busan", "Sokcho"]):
        break
    else:
        print("값이 잘못 입력 되었습니다.")

graph = {
    "Seoul": {"Wonju": 88, "Daejeon": 140, "Gwangju": 270, "Sokcho": 168},
    "Wonju": {"Seoul": 88, "Sokcho": 110, "Daejeon": 120, "Busan": 260},
    "Daejeon": {"Wonju": 120, "Seoul": 140, "Gwangju": 200, "Busan": 200},
    "Gwangju": {"Daejeon": 200, "Seoul": 270, "Busan": 200},
    "Busan": {"Gwangju": 200, "Daejeon": 200, "Wonju": 200, "Sokcho": 340},
    "Sokcho": {"Seoul": 168, "Wonju": 110, "Busan": 340},
}

print(f"찾으시는 {start}부터 {end}까지의 거리는 {solve(graph)}Km 입니다.")
