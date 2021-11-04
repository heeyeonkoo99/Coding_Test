# key point: DFS를 사용해 방문 처리를 하자
# graph 리스트에서 0은 아직 방문 X, 1은 방문 완료했다는 의미로 사용

#데이터 입력받아서
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 최대한 멀리 가면서 1이 나올때까지 탐색, 1이 나오면 종료하고 다음 노드로
def dfs(x, y):
    #주어진 범위를 벗어날 경우 False
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    #(x,y)에 방문하지 않았으면
    if graph[x][y]==0:
        # (x,y) 방문 처리
        graph[x][y]=1
        # (x,y)의 상하좌우에 있는 노드들을 확인 -> dfs를 거치면서 하나씩 방문 처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):            
            # 방문 처리 안된 노드들은 상하좌우 dfs로 확인한 후 True 반환 
            result +=1
        # 방문처리된 노드들은 False 반환하여 스루할 수 있음

print(result)