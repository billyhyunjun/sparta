import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")
import heapq


n, m = map(int, input().split())

heap = []
for i in map(int, input().split()):
    heapq.heappush(heap, i)

while m > 0:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a + b)
    heapq.heappush(heap, a + b)
    m -= 1

print(sum(heap))
