# 목표가 되는 값 입력
x = int(input())
# 반복문 실행 1부터 x+1 까지 목록 생성 (x값 까지 포함 할려면 x+1)해야함
for i in range(1, x+1):
    # 번호 뜯어서 합치기 123이면 [1,2,3]으로 나옵니다.
    num = sum(map(int,str(i)))   # 문자열로 해주어야지 글자 때짐
    # 생성자 값이랑 분해값 합치기
    total = i + num

    # 만들어진 값이 입력했던 값이랑 같다면 가장 작은 값만 가져오면 되니 거서 끝!!출력하고 반복문 탈출
    if x == total:
        print(i)
        break
    # 입력값이 i값과 같으면 없는거니깐 0으로 출력
    if i == x:
        print(0)