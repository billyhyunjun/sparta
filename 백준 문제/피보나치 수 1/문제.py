import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

count1 = 0
count2 = 0


def fib(num):
    global count1
    if num == 1 or num == 2:
        count1 += 1
        return 1  # 코드1
    else:
        return fib(num - 1) + fib(num - 2)


def fibonacci(num):
    global count2
    f = [0] * (num + 1)
    f[1] = f[2] = 1
    for i in range(3, num + 1):
        count2 += 1
        f[i] = f[i - 1] + f[i - 2]  # 코드2
    return f[num]


n = int(input())
fib(n)
fibonacci(n)
print(count1, count2)

