import sys
input = sys.stdin.readline
INF=int(1e9)

#floyd warshall algorithm

#n: 회사의 개수, m: 경로의 개수
n, m = map(int, input().split())

# 회사의 개수만큼 이차원 배열 생성하여 최소 경로 저장하도록 함
graph = [[INF]*(n+1) for _ in range(n+1)]

# 현재 회사->현재회사 일 경우 이동할 필요 없으므로 0
for a in range(1, n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 입력받은 연결된 회사들의 경로 저장해두기 (양방향, 이동비용 모두 1)
for i in range(m):
    f, t = map(int, input().split())
    graph[f][t], graph[t][f]=1,1

# x: 물건 판매 회사, k: 소개팅
x, k = map(int, input().split())

#플로이드 워셜로 최소 비용 그래프 갱신하여 저장
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][i]+graph[i][b])

#1번-> k번 -> x번으로 이동하는 최소 경로를 구해야 한다!
#1->k 또는 k->x의 경로가 없을경우 -1 반환
if graph[1][k]==INF or graph[k][x]==INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])


  