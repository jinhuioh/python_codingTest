import time
# time.time() 으로 코드에 소요되는 시간을 측정할 수 있다.
# 실행코드 맨 앞과 맨 뒤에 시간측정을 하여 총 몇초가 걸리는지 판단하고
# 최소시간이 소요되도록 코드를 구현하는 것이 좋다.
# 이중포문 등으로 복잡하게 코드를 구현할 경우 (실행 경우의 수가 많아질수록) 소요시간이 증가한다.

# 측정 시작 시간
start_time = time.time()

# 프로그램 소스코드
n, k = map(int, input().split())
i=0
if (2<=n<=100000)&(2<=k<=100000):
    while n<=k:
        # n=1이면 break
        if n == 1:
            # print('n1',n)
            break
        # n을 k로 나누었을때 나머지가 0이면 n/k를 n에 덮어씌우기(2번)
        elif n%k == 0:
            i += 1
            n = n/k
            # print('n2',n)
        # n을 k로 나눌수 없는 경우 -1 연산(1번)
        else :
            i += 1
            n = n-1
            # print('n3',n)

# 측정 종료 시간
end_time = time.time()
# 측정시간 프린트
print(start_time, end_time)