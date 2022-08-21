# 정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
# 경우의 수를 구하는 프로그램을 작성하시오.
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
# 00시00분03초
# 00시13분30초

# 입력조건
# 첫째 줄에 정수 n이 입력된다.(0~23사이)
#출력조건
# 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

# # n입력받기
n = int(input())
# count 할 객체
num = 0
# i는 시간
for i in range(n+1):
    # j는 분
    for j in range(60):
        # k는 초
        for k in range(60):
            # 문자중에 3이 하나라도 있으면 num+1
            if '3' in str(i) + str(j) + str(k):
                num += 1
                # print(str(i) + str(j) + str(k))
print(num)