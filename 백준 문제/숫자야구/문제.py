import sys
from itertools import permutations

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")


t = int(input())
for _ in range(t):
    num, s, b = map(int, input().split())

num_list = list(map(int, permutations(range(1, 10), 3)))

print(num_list)

