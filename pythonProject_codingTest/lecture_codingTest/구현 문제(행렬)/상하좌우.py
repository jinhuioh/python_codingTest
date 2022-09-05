# 상하좌우
# 입력조건

# 첫째줄에 공간의 크기를 나타내는 N이 주어진다.
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다.
# L:왼쪽 1칸, R:오른쪽 1칸, U:위로 1칸, D:아래로 1칸
# 최소가(1,1)이므로 0의 값은 없다.
# 입력조건====
# 첫째 줄에 공간의 크기를 나타내는 n이 주어진다.
# 둘째줄에 여행가 A가 이동할 계획서 내용이 주어진다.(L R R U)
# 출력조건====
# 최종적으로 도착할 지점의 좌표(x,y)를 공백으로 구분하여 추출한다.
# 시작은(1,1)이고 x가 행의 이동(상하), y가 열의 이동(좌우)

# 움직일 횟수 받기
n = int(input())
# 움직일 데이터 받기
# lambda로 n개만 받는걸로 수정해보기!
move = list((input().split()))
print(move)
# move = [L, R, R, U]
# 행렬문제를 백터를 생성해주자!
dx = [0,-1,0,1]#좌우
dy = [1,0,-1,0]#상하
xy = ['U','L','D','R']
x = 1
y = 1

for move_one in move:
    for i in range(len(xy)):
        if move_one == xy[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx)
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx, ny
print(x,y)