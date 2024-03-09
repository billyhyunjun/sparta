import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

# 테스트 숫자 입력
test = int(input())
# 테스트 숫자 만큼 반복
for _ in range(test):
    # 입력 값을 단어마다 나누어서 리스트화
    n = list(input())
    # 계산을 도와줄 통
    stack = []

    for i in n:

        if i == ")" and stack:
            stack.pop()

        elif i == "(":
            stack.append(i)

        else:
            stack.append(i)
            break

    if not stack:
        print("YES")

    else:
        print("NO")










    # # 입력 값을 단어마다 나누어서 리스트화
    # n = list(input())
    # # 계산을 도와줄 통
    # num = 0
    # # 반복문에 들어가서 비교하기
    # for i in n:
    #     # (이라면 +1  )이라면-1을 해서 0이되면 괄호가 닫힌 것이다
    #     if i == "(":
    #         num += 1
    #     elif i == ")":
    #         num -= 1
    #         # 만약에 이미 괄호가 완성이 되어서 0인 상테에 )가 들어오면 -1이 되므로 잘못된 괄호 이므로 아웃
    #         if num < 0:
    #             break
    # # 괄호가 모두 잘되어 있으면 yes
    # if num == 0:
    #     print("YES")
    # # 괄호가 부적합이면 no
    # else:
    #     print("NO")
