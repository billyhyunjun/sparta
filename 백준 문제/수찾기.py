# 숫자 갯수 입력 (파이썬 에서는 없어도 작동에 문제가 없다...)
n = int(input())
# 리스트 받아 오기
numbers = list(map(int, input().split()))

# 리스트에 있는 숫자를 번호 적힌 깃발로 만들기
for i in numbers:
    globals()["num_flag{}".format(i)] = True

# 정답 입력 받기
m = int(input())
select = list(map(int, input().split()))

# 정답 번호의 깃발을 찾을 때 깃발이 True 라면 1 없으면 오류가 뜨니 except 로 빼서 0
for i in select:
    try:
        if globals()["num_flag{}".format(i)]:
            print("1")
    except KeyError:
        print("0")
