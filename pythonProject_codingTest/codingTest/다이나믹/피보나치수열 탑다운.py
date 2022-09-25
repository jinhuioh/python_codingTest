# 반복문제(계산)에 적합한 활용. 부분문제가 중복되는 경우에 다이나믹 프로그래밍 유형임을 파악하자!!
# 탑다운(메모이제이션: 이전 값을 저장해두고 꺼내씀으로써 연산과정을 최대한 단축시키는 방법(캐싱)이라고도 한다.)
# 하향식방법
# 보텀업 방식은 상향식 방법

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1혹은 2일때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산 한 적 있는 문자라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return  d[x]
print(fibo(99))