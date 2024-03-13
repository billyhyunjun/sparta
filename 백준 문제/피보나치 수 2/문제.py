import sys
# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def fib(num):
    if num < 2:
        return num
    fib_list = [0, 1]
    for i in range(2, num + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[num]


n = int(input())
print(fib(n))

