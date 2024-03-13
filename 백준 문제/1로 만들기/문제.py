import sys
# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")


def make_one(num):
    if num == 1:
        return 0
    count_list = [0, 0]
    for i in range(2, num + 1):
        if i % 3 == 0 and count_list[i // 3] + 1 <= count_list[i // 2] + 1 and count_list[i // 3] + 1 <= count_list[i - 1] + 1:
            count_list.append(count_list[i // 3] + 1)
        elif i % 2 == 0 and count_list[i // 2] + 1 <= count_list[i - 1] + 1:
            count_list.append(count_list[i // 2] + 1)
        else:
            count_list.append(count_list[i - 1] + 1)
    return count_list[num]


n = int(input())
print(make_one(n))