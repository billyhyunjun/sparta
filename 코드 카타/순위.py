def make_result(graph):
    for i in range(1, len(graph)):
        for j in graph[i]:
            for k in graph[j]:
                if k not in graph[i]:
                    graph[i].append(k)
    return graph


def solution(n, results):
    graph_win = [[] for _ in range(n+1)]
    graph_lose = [[] for _ in range(n+1)]

    for i in results:
        graph_win[i[0]].append(i[1])
        graph_lose[i[1]].append(i[0])

    graph_win = make_result(graph_win)
    graph_lose = make_result(graph_lose)

    counter = 0
    for i in range(n+1):
        if len(graph_win[i]) + len(graph_lose[i]) == n-1:
            counter += 1
    return counter


a = 5
b = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# c = 3
# result = solution(a)
result = solution(a, b)
# result = solution(a, b, c)
print(result)
