# 파이썬은 한줄로 조건문을 써도 된다.
score = 85
if score >= 80: result = 'success'
else: result = 'fail'
print(result)

# while문
i=1
result=0
while i<=9:
    result +=i
    i+=1
print(result)

a = [9,8,7,5,4]
for x in a:
    print(x, end=" ")#end 안쓰면 한 줄에 한 문자씩 출력됨


# 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때
# continue를 사용
# 1부터9까지 홀수의 합을 구할 때 아래와 같이 작성할 수 있다.
result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    result +=i
print('\n',result)

# 이중포문
# 구구단
i,x = 1,0
for i in range(1,11):
    for x in range(0,9):
        x+=1
        print(i,' x ',x,' = ',i*x)

