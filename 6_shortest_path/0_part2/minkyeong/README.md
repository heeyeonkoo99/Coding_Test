# 🛒Shortest Path
## Dijkstra Algorithm

- 한 지점에서 다른 특정 지점까지의 최단 경로 구할 때 사용

- 가장 처음 노드부터 시작, 이어져있지 않다면 (int)1e9로 초기화

- 현재 노드로부터 아직 방문하지 않은 노드들 사이의 최소 비용을 계산하여 테이블에 저장

- 최소 비용을 가진 노드로 이동하여 그 노드로부터 아직 방문하지 않은 노드들까지의 최소 비용을 계산하여 테이블 업데이트

- O(E logV) *E: edges V: vetices

```python
import heapq
import sys

input = sys.stdin.readline
INF=int(1e9)
n,m= map(int, input().split())
start = int(input())
graph=[[] for i in range(m)]
distance = [INF]*(m+1)
q=[]

for _ in range(m):
    #a 노드부터 b 노드까지의 비용 : c
    a,b,c=map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        #시작 노드부터 현재노드까지의 최소 비용, 현재 노드
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 우선순위큐에 저장된 최소비용이 최소가 아니라면 스킵
            continue
        for i in graph[now]: #현재 노드의 엣지 모두 확인해서 최소 비용 갱신
            cost = dist+i[0]
            if cost<distance[i[0]]: #기존 값보다 작으면 갱신
                distance[i[0]]=cost
                heapq.heappush(cost, i[0])

```

## Floyd-warshall Algorithm

- 모든 지점에서 다른 모든 지점까지의 최단 경로 찾을 때 사용

- 다이나믹 프로그래밍

- min(A->B의 비용, A->K->B의 비용)
   
- O(V^3)