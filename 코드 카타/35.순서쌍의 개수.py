def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer
#----제곱근 이용---
# def solution(n):
#     answer = 0
#     for i in range(1,int(n**0.5)+1):
#         if n%i==0:
#             answer+=1
#     return answer*2-1 if n**0.5==int(n**0.5) else answer*2

a = 100000
# b = 10
# c = 3
result = solution(a)
print(result)
