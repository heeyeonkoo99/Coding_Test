from collections import deque
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# x,y까지 걸리는 경로의 값들을 graph[x][y]에 업데이트
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인 
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # nx, ny가 범위를 벗어났을 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue

            #이미 방문했으면 무시
            if graph[nx][ny] == 0:
                continue
            # 아직 방문 안했으면 현재에서 1칸 움직였다고 판단 -> 현재+1 값 저장
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))


