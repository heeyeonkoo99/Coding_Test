from collections import deque

##### 입력 처리 #####
N = int(input()) # map 크기
K = int(input()) # 사과 개수
matrix = [[0] * N for _ in range(N)] #map 이차원 배열

for _ in range(K):
    x, y = map(int, input().split())
    matrix[x-1][y-1]=1 # map 배열에 사과 위치 update (1행 1열부터 시작하므로 -1 처리)

c = int(input()) # 방향 전환 횟수 입력
change = {}
for _ in range(c): # 방향 전환하는 초, 회전방향 dictionary에 저장
    int_x, ch = input().split()
    change[int(int_x)]=ch

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

d = 1 # 방향(북(0), 동(1), 남(2), 서(3) 순서)
x, y = 0, 0 # 좌표계 위치

# 방향 전환 함수
def change_direction(direction, d):
    if direction == 'D':
        d = (d+1)%4
    else:
        d = (d-1)%4
    return d

snake = deque([(0,0)])
t = 0
while True:
    # 1초 증가
    t += 1
    # 좌표 update
    x += dx[d]
    y += dy[d]
    if t in change.keys(): #방향 전환에 해당하는 초이면, 방향 전환
        d = change_direction(change[t], d)
    if x<0 or y<0 or x>=N or y>= N: #좌표가 map에서 벗어나면 종료
        break
    if [x,y] in snake: # 자기 자신과 부딪히면 종료
        break
    if matrix[x][y]==1: # 사과 있을 경우
        matrix[x][y]=0
        snake.append([x,y])
    else: # 사과 없을 경우
        snake.append([x,y])
        snake.popleft()

print(t)