coin, money = map(int, input().split())

price = []
for i in range(coin):
    price.append(int(input()))

price.sort(reverse=True)

count = 0

for i in price:
    if money >= i:
        count += money // i  # 나눌수 있는 값
        money %= i  # 나누고 남은 값
        if money == 0:  # 나머지가 0이면 끝내기
            break

print(count)