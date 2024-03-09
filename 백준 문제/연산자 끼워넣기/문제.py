import sys

# 표준 입력을 파일로 설정
sys.stdin = open("input.txt", "r")

# 테스트 반복 !
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    numbers = list(map(int, input().split()))
    tools = list(map(int, input().split()))

    max_value = -1000000000
    min_value = 1000000000


    def find_value(num_count, value, plus, minus, multiply, divide):

        global max_value, min_value

        if num_count == num:
            max_value = max(value, max_value)
            min_value = min(value, min_value)
            return

        if plus > 0:
            find_value(num_count + 1, value + numbers[num_count], plus - 1, minus, multiply, divide)
        if minus > 0:
            find_value(num_count + 1, value - numbers[num_count], plus, minus - 1, multiply, divide)
        if multiply > 0:
            find_value(num_count + 1, value * numbers[num_count], plus, minus, multiply - 1, divide)
        # 이거 나누는 법을 잘 알아야한다 -5에서 2를 //로 나누면 내림이 적용이 되서 값이 -3이 나온다... 그래서 int 써야함
        if divide > 0:
            find_value(num_count + 1, int(value / numbers[num_count]), plus, minus, multiply, divide - 1)


    find_value(1, numbers[0], tools[0], tools[1], tools[2], tools[3])
    print(max_value)
    print(min_value)

    # # 입력 받기
    # N = int(input())
    # # 숫자 열
    # num = list(map(int, input().split()))
    # # 각 연산자들
    # op = list(map(int, input().split()))  # +, -, *, //
    #
    # # 최고 값을 받기 위해서 가장 낮은 값 설정
    # maximum = -1e9
    # # 최저 값을 받기 위해서 가장 높은 값 설정
    # minimum = 1e9
    #
    # # ( 현재 사용중인 숫자 갯수, 현재의 값, 각각 더하기, 빼기, 곱하기, 나누기 남은 횟수)
    # def dfs(depth, total, plus, minus, multiply, divide):
    #     global maximum, minimum
    #     # 숫자 사용 횟수가 다 찾을 때 끝내기
    #     if depth == N:
    #         # 지금 까지의 최고 값과 계산 했을 때 계산 값을 비교 큰 값을 넣어 주라
    #         maximum = max(total, maximum)
    #         # 지금 까지의 최저 값과 계산 했을 때 계산 값을 비교 작은 값을 넣어 주라
    #         minimum = min(total, minimum)
    #         return
    #     # 더하기 횟수가 남아 있다면 실행
    #     if plus:
    #         dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    #     # 빼기 횟수가 남아 있다면 실행
    #     if minus:
    #         dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    #     # 곱하기 횟수가 남아 있다면 실행
    #     if multiply:
    #         dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    #     # 나누기 횟수가 남아 있다면 실행
    #     if divide:
    #         dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)
    #
    # # dfs입장 1번 부터 가지고 갑니다, 현재 값은 0, 각각의 도구 횟수 입력
    # dfs(1, num[0], op[0], op[1], op[2], op[3])
    # # 결과
    # print(maximum)
    # print(minimum)
