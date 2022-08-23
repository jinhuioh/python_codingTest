# 리스트
import time

n = 10
# a = 길이가 n인 0이 들어있는 리스트
a = [0] * n
print(a)

# 인덱싱과 슬라이싱
a = [1,2,3,4,5,6,7,8]
# 슬라이실
print(a[1:4])

i=0
# i를 0부터 9까지 배열에 넣어서 만들기
array = [i for i in range(10)]
print(array)

# 리스트 컴프리헨션 방법
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
h1 = time.time()
array1 = [i for i in range(20) if i % 2 == 1]
print('array1',array1)
h2 = time.time()
print('리스트컴프리헨션 수행시간: ', h1,h2)

# 일반적인 방법
h3 = time.time()
array2 = []
for i in range(20):
    if i % 2 ==1:
        array2.append(i)
h4 = time.time()
print('array2',array2)
print('일반적인 코드 수행시간: ', h3,h4)

# 리스트에서 원소가 1인 개수 세기
con = array1.count(1)
print(con)

a = [1,2,3,4,5,5,5,5]
remove_set = {3,5}#집합자료형
result = [i for i in a if i not in remove_set]
print('result:',result)

# n*m 크기의 2차원 리스트를 초기화할 때
# 길이가m인 리스트를 n개 만들기
n,m = map(int,input().split())
# 변수값을 무시하고자 할 때 언더바_를 사용
array3 = [[0]*m for _ in range(n)]
print(array3)
