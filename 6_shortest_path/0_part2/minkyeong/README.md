# ๐Shortest Path
## Dijkstra Algorithm

- ํ ์ง์ ์์ ๋ค๋ฅธ ํน์  ์ง์ ๊น์ง์ ์ต๋จ ๊ฒฝ๋ก ๊ตฌํ  ๋ ์ฌ์ฉ

- ๊ฐ์ฅ ์ฒ์ ๋ธ๋๋ถํฐ ์์, ์ด์ด์ ธ์์ง ์๋ค๋ฉด (int)1e9๋ก ์ด๊ธฐํ

- ํ์ฌ ๋ธ๋๋ก๋ถํฐ ์์ง ๋ฐฉ๋ฌธํ์ง ์์ ๋ธ๋๋ค ์ฌ์ด์ ์ต์ ๋น์ฉ์ ๊ณ์ฐํ์ฌ ํ์ด๋ธ์ ์ ์ฅ

- ์ต์ ๋น์ฉ์ ๊ฐ์ง ๋ธ๋๋ก ์ด๋ํ์ฌ ๊ทธ ๋ธ๋๋ก๋ถํฐ ์์ง ๋ฐฉ๋ฌธํ์ง ์์ ๋ธ๋๋ค๊น์ง์ ์ต์ ๋น์ฉ์ ๊ณ์ฐํ์ฌ ํ์ด๋ธ ์๋ฐ์ดํธ

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
    #a ๋ธ๋๋ถํฐ b ๋ธ๋๊น์ง์ ๋น์ฉ : c
    a,b,c=map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        #์์ ๋ธ๋๋ถํฐ ํ์ฌ๋ธ๋๊น์ง์ ์ต์ ๋น์ฉ, ํ์ฌ ๋ธ๋
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # ์ฐ์ ์์ํ์ ์ ์ฅ๋ ์ต์๋น์ฉ์ด ์ต์๊ฐ ์๋๋ผ๋ฉด ์คํต
            continue
        for i in graph[now]: #ํ์ฌ ๋ธ๋์ ์ฃ์ง ๋ชจ๋ ํ์ธํด์ ์ต์ ๋น์ฉ ๊ฐฑ์ 
            cost = dist+i[0]
            if cost<distance[i[0]]: #๊ธฐ์กด ๊ฐ๋ณด๋ค ์์ผ๋ฉด ๊ฐฑ์ 
                distance[i[0]]=cost
                heapq.heappush(cost, i[0])

```

## Floyd-warshall Algorithm

- ๋ชจ๋  ์ง์ ์์ ๋ค๋ฅธ ๋ชจ๋  ์ง์ ๊น์ง์ ์ต๋จ ๊ฒฝ๋ก ์ฐพ์ ๋ ์ฌ์ฉ

- ๋ค์ด๋๋ฏน ํ๋ก๊ทธ๋๋ฐ

- min(A->B์ ๋น์ฉ, A->K->B์ ๋น์ฉ)
   
- O(V^3)