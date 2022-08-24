# 함수
# def 함수명(매개변수):
#     실행할 코드
#     return 반환 값

# 더하기함수만들기
def add(a,b):
    return a+b

print(add(5,10))
# 아래와 같이 파라미터 변수를 직접 지정하여 값을 넣어줄 수 있다.
print(add(b=8,a=2))

# global 키워드
# 해당 함수에서 지역 변수를 만들지 않고 함수 바깥에 선언된 변수를 참조하게 된다.
a = 10
def fun():
    global a #global a 가 없으면 a+=1에 오류가 남
    a +=1
    print(a)
fun()

# 리스트에 append하기
arr = [1,2,3,4,5]
def func():
    arr.append(6)
    print(arr)
func()

# 여러개의 반환값 변환
# 사칙연산 하기
def operator(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    return  add, sub, mul

print(operator(3,7))

# 람다 표현식
# 함수를 한 줄에 간단하게 작성 가능
# :(콜론)뒤에 리턴 값 입력
print((lambda a,b : a+b)(3,7))


# 학생과 점수가 나와있는 튜플형태의 리스트를 점수가 낮은 순서부터 차례대로 정렬해보자.
# sorted(정렬할 데이터, key파라미터)
array=[('홍',50),('진',34),('이',90)]
def my_key(x):
    return x[1]#key부분(점수)을 리턴
print(sorted(array, key=my_key))

# 람다를 사용해서 아래와 같이 간편하게 출력할 수 있다.
print(sorted(array,key=lambda x:x[1]))

# 2개의 리스트를 순서대로 더하는 방법
list1 = [1,2,3,4,5]
list2 = [11,22,33,44,55]
# 매개변수 a,b의 더한값을 리턴하고 list1과 list2에 적용시킨다.
result = map(lambda a,b:a+b, list1, list2)
print(list(result))