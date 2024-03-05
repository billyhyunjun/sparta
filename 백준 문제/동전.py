# 동전 종류랑 총합 돈
coin, money = map(int, input().split())
# 동전 종류별 각 금액 적는 통
price = []
# for문으로 반복 입력 받기
for i in range(coin):
    # 입력 받고 바로 리스트 추가
    price.append(int(input()))
# 비싼 금액을 0번부터 차례대로 줄지어 주기
price.sort(reverse=True)
# 동전 사용 횟수 카운트
count = 0
# 동전 리스트 별로 큰 금액부터 차례대로 사용가능한지 보기
for i in price:
    # 만약에 전체금액보다 내가 사용할 동전의 가치가 낮다면 동전 써서 내기
    if money >= i:
        count += money // i  # 해당 금액에 맞추어 나눌수 있는 값 = 사용한 동전 갯수
        money %= i  # 나누고 남은 값
        if money == 0:  # 나머지가 0이면 끝내기
            break

print(count)