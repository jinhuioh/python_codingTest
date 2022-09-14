##BFS문제(미로문제, 터널문제, 너비탐색(선입선출))
# 동빈이는 n*m 크기의 직사각형 형태의 미로에 갇혔습니다.
# 미로를 탈출해야 합니다.
# 동빈이의 위치는(1,1)이며 미로의 출구는 (n,m)의 위치에 존재하며 한 번에 한 칸씩 이동가능합니다.
# 이때 괴물이 위치한 부분은 0 없는 부분은 1로 되어있습니다.
# 미로는 반드시 탈출 할 수 있는 형태로 제시됩니다.
# 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.
#
# 입력조건: 첫째 줄에 두 정수 n,m(4<=n, m<=200)이 주어집니다.
# 다음 n개의 줄에는 각각 m개의 정수(0또는 1)로 미로의 정보가 주어집니다.
# 각각 수들은 공백 없이 입력으로 제시됩니다. 또한 시작 칸과 마지막 칸은 항상 1입니다.
# 출력조건: 첫째 줄에 최소 이동 칸의 개수를 출력합니다.
# ##
# 큐
# 큐 넣기(맨뒤에 원소1삽입)=enqueue =파이썬의 append()
# 큐 빼기(맨 앞에서 원소1개 빼내기)=dequeue=파이썬의 popleft()
from collections import deque

# 선입선출로 입구와 출구가 터널 형태로 되어있는 문제는 queue 함수를 이용한다.

# 행렬입력받기
n,m = map(int,input().split())
# 그래프 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 상하좌우로 움직일 좌표
dx = [-1,1,0,0]#좌우
dy = [0,0,-1,1]#상하

# 함수화
def bfs(x,y):
    # 큐 함수 임포트해서 x,y좌표 넣기
    queue = deque()
    # 큐에 현재 위치 넣기
    queue.append((x,y))
    while queue:
        # 큐에 넣은 위치를 하나씩 빼서 while문으로 위치 연산
        x, y = queue.popleft()
        for i in range(4):
            # 상하좌우로 이동
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프 범위를 넘어서면 continue(위치가 0인 것 보다 범위를 넘어서는 continue 되는 것이 먼저 실행 되어야 한다.)
            # 위치가 0이면 continue
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                # 원래 위치에서 다음 위치로 이동할 때 +1을 해줌.
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[m-1][n-1]
print(bfs(0,0))
