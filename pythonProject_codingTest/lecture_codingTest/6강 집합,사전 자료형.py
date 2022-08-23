# 사전 자료형
# 키벨류 값의 쌍을 데이터로 가지는 자료형
# 데이터 조회 및 수정에 있어서 빠르게 처리가 가능하다.

# dict는 초기화 함수
data = dict()
data['key'] = 'value'
data['사과'] = 'apple'

# 딕셔너리 객체가 출력
print(data)

if '사과' in data:
    print('\'사과\'를 key로 가지는 데이터가 존재')

# key객체들만 출력해보자
key_list = data.keys()
print('keys: ', key_list)

# value객체들만 출력해보자.
value_list = data.values()
print('values: ', value_list)

# 아래와 같이 객체를 초기화 하고 다른 값을 넣을 수 있다.
data = {
    '사과':100,
    '바나나':200
}
print(data)

# /////////////////////////////////////////////
#집합자료형
# 중복 안됨
# 순서 없음
# 합,교,차집합 연산 가능

# 집합 자료형 초기화 방법
data = set([1,1,2,2,2,2,3,4,5,5,5])
print(data)#중복은 없어지고 집합 형태로 리스트가 변경된 것을 확인 가능

# 집합 자료형 초기화 방법
data = {1,1,2,2,2,3,3,4}
print(data)

# 추가
data.add(100)
print(data)

# 여러개 추가
data.update([200,300])
print(data)

# 삭제
data.remove(100)
print(data)