import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

from collections import deque, defaultdict


def printer(paper, imp, value):
    counter = 0
    while paper:
        if imp[0] == max(imp):
            if paper[0] == value:
                return counter + 1
            paper.popleft()
            imp.popleft()
            counter += 1
        else:
            paper.append(paper.popleft())
            imp.append(imp.popleft())


T = int(input())
for _ in range(T):

    num, index = map(int, input().split())
    papers = deque()
    importance = deque()

    for i in range(num):
        papers.append(i)
    for i in map(int, input().split()):
        importance.append(i)
    index_value = papers[index]

    print(printer(papers, importance, index_value))



