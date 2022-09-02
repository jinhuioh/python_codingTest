#n이 1이 될 때까지----------------------------------------------------------------
# 어떤 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고한다
# 단 두번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

# 입력조건
# 첫째 줄에 N(2<=N<=100000), K(2<=K<=100000)가 공백으로 구분되며 각각 자연수로 주어진다.
# 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

# 출력조건
# 첫째 줄에 N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.

# N과K를 입력받자

# n,k = map(int, (input().split()))
# count = 0
# while n is not 1:
#     if n == 1:
#         break
#     if n%k != 0:
#         n -= 1
#         count += 1
#     else:
#         n = n//k
#         count +=1
# print(count)

n,k = map(int, (input().split()))
result = 0
while True:
    # n이k보다 작아서 더이상 나눌 수 없을 때 반복문 탈출
    if n < k:
        break
    # n을 k로 나누어 떨어지는 수가 될때까지 빼기
    #11 2를 입력하면 target을 10으로 정해서 빼기를 총 1번만 하면 됨
    #그 값을 result에 넣으면 총 빼기 한 연산 개수가 담김
    target = (n // k) * k
    # n이k의 배수이면 result=0 이 된다.
    result += (n - target)
    print('첫번째',result)
    # 빼기를 한 나머지가 n이 됨
    n = target
    # # n이k보다 작아서 더이상 나눌 수 없을 때 반복문 탈출
    # if n < k:
    #     break
    # n이 k보다 큰 경우 n//k실행
    n = n//k
    result += 1
    print('두번째',result)
# 마지막으로 남은 수에 대해 1씩 빼기
result
print(result)