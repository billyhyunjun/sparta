import sys

# 표준 입력을 파일로 설정
# sys.stdin = open("input.txt", "r")
import heapq


n = int(input())

heap = []


while n > 0:
    a = int(sys.stdin.readline())
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, a)
    n -= 1


