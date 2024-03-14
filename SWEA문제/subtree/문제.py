import sys
# from collections import deque

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def subtree(node):
    global result
    if node:
        result += 1
        subtree(graph[node][0])
        subtree(graph[node][1])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    e, n = map(int, input().split())

    graph = [[0, 0] for _ in range(e + 2)]
    # x의 값을 리스트로 변경시켜준다.
    x = list(map(int, input().split()))
    # 홀수 번은 노드의 번호 짝수 번은 연결된 노드를 표시하니 2씩 증가하면서 그래프에 값을 넣어주면 됩니다.
    for i in range(0, len(x), 2):
        if graph[x[i]][0] == 0:
            graph[x[i]][0] = x[i+1]
        elif graph[x[i]][1] == 0:
            graph[x[i]][1] = x[i+1]

    result = 0

    subtree(n)
    print(f"#{test_case} {result}")


    # ------큐 설정 이건 이진 트리가 아니다 ㅋㅋ------
    # queue = deque()
    # # e = 노드 연결 횟수 (총 노드는 e+1개)
    # # n = 루트 노드로 선택 할 것 그 밑에 있는 값을 전부 세어보자
    # e, n = map(int, input().split())
    # # 총노드 갯수가 e+1개에다가 1번 부터 쓰고 싶으니깐 앞에 빈칸 합쳐서 e+2개를 만들어준다.
    # graph = [[] for _ in range(e+2)]
    # # x의 값을 리스트로 변경시켜준다.
    # x = list(map(int, input().split()))
    # # 홀수 번은 노드의 번호 짝수 번은 연결된 노드를 표시하니 2씩 증가하면서 그래프에 값을 넣어주면 됩니다.
    # for i in range(0, len(x), 2):
    #     graph[x[i]].append(x[i+1])
    # # 시작할 번호를 큐에 넣어준다.
    # queue.append(n)
    # # 본인을 포함 자식노드가 몇개가 있는지 횟수 탐색
    # counter = 0
    #
    # # 반복문 진행
    # while queue:
    #     # 큐안에 있는 값 꺼내기
    #     x = queue.popleft()
    #     # 꺼내면서 카운트 1증가
    #     counter += 1
    #     # 해당노드에 있는 번호 전부 큐에 넣기 이 문제의 특성상 되돌아가는 방향은 없기 때문에 방문 표시는 안해도 됩니다.
    #     for i in graph[x]:
    #         queue.append(i)
    # # 결과 출력
    # print(f"#{test_case} {counter}")