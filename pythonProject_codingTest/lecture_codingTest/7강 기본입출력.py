# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# 공백을 기준으로 구분 된 데이터를 입력받을 때 (n개)
# list(map(int,input().split()))
# 공백을 기준으로 구분 된 몇 개의 데이터를 입력받을 때 (정해진 개수)
# a,b,c = map(int,input().split())
import sys

# 성적을 n개를 입력받아서 내림차순으로 출력하는 프로그램은 아래와 같다.
data = list(map(int,input().split()))
data.sort(reverse=True)#내림차순
print(data)

# 딱 n개의 원소만 입력 받는 방법
n = int(input())
i = input().split()
data = [i for i in range(n)]
data.sort(reverse=True)#내림차순
print(data)

# 리스트를 n개만 입력받는 방법(리스트안에 리스트n개가 들어있는 형태)
n = int(input())
#입력을 원하는 대로 받아서 리스트에 넣고, n번 반복
data = [input().split() for i in range(n)]
data.sort(reverse=True)#내림차순
print(data)

# 사용자로부터 빠르게 입력받기
# input보다 빠른방법
# sys라이브러리에 있는 sys.stdin.readline() 메서드 이용
# 입력 후 엔터가 줄바꿈 기호로 입력되므로 rstrip()메서드를 함께 사용
data = sys.stdin.readline().rstrip()
print(data)

# 출력 end사용법
# 줄바꿈을 원치않을때 사용
print(7, end=" ")
print(8, end=" ")
# 7 8 로 출력되는 것을 확인 할 수 있다.