# 그리디 알고리즘: 현 상황에서 지금 당장 좋은 것만 고르는 방법을 의미
# 당신은 음식점의 계산을 도와주는 점원이다.
# 카운터에는 거스름돈으로 사용할 500, 100, 50, 10원짜리 동전이 무수히 존재한다고 가정한다.
# 손님에게 거슬러 줘야 할 돈이 N원일때 거슬러 줘야할 동전의 최소 개수를 구하시오.
# 단 거슬러 줘야할 돈은 항상 10의 배수이다.
n = int(input())
count=0
# 큰 단위 화폐부터 차례대로 확인하기
array = [500,100,50,10]

for coin in array:
    count = count + (n // coin)#거스름돈을 동전으로 나누었을 때의 몫을 count에 넣기
    n = n % coin##동전으로 나눈 나머지를 n에 넣어서 for문 돌려서 계속 빼주기.
print(count)




# 내가 푼 방법
# 입력받은 거스름돈 N
N = int(input())
# 풀이: 큰 수부터 차례로 빼주자.
c=0
while N :
    if (N-500)<0:
        break
    N = N-500
    c=c+1
print('500원개수'+c)

while N :
    if (N-100)<0:
        break
    N = N-100
    c=c+1
print(c)

while N :
    if (N-50)<0:
        break
    N = N-50
    c=c+1
print(c)
while N :
    if (N-10)<0:
        break
    N = N-10
    c=c+1
print('총 동전 개수'+c)