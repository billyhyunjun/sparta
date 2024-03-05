# 값 입력
x = int(input())
# 반복문 실행 1부터 x까지 목록 생성
for i in range(1,x+1):
    # 번호 뜯어서 합치기
    num = sum(map(int,str(i)))
    # 생성자 값이랑 분해값 합치기
    total = i + num

    # 값이 같다면 출력하고 반복문 탈출
    if x == total:
        print(i)
        break
    # 없으면 0으로 출력
    if i == x:
        print(0)