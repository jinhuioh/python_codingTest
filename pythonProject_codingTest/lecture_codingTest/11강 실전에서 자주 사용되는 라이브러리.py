# min max함수
from collections import Counter
from itertools import permutations, combinations

min_result = min(1, 2, 3, 4, 5)
print(min_result)

# sorted함수
array = [('홍', 50), ('진', 34), ('이', 90)]
# 점수순으로  내림차순 정렬
sorted_jumsu = sorted(array, key=lambda x: x[1], reverse=True)
print(sorted_jumsu)

# 순열과 조합
# 순열은 순서있음, 조합은 순서 없음
# permutations함수를 이용하여 a,b,c의 모든 순열을 구해보자.
data = ['a', 'b', 'c']
result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)

result = list(combinations(data, 2))  # data에서 2개를 뽑는 모든 조합 구하기
print(result)

# counter함수
# 리스트와 같은 반복가능한 객체가 주어졌을 때 내부 원소가 몇 번씩 등장했는지 알려줌
counter = Counter(['r','r','b','g','b','c'])
print(counter['r'])
print(counter['g'])
print(dict(counter))#사전 자료형으로 변환

# 최대 공약수
# gcd()함수 이용
# 최소 공배수
# lcm()함수 이용