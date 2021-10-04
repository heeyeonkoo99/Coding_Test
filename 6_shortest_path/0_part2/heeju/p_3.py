import heapq

INF=int(1e9)

n,m,c=map(int,input().split())

graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
  d,e,f=map(int,input().split())
  graph[d].append((e,f))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dis,now=heapq.heappop(q)
    if distance[now]<dis:
      continue
    for i in graph[now]:
      cost=dis+i[0]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(c)

cnt=0
maxTime=0

for d in distance:
  if d!=INF:
    cnt+=1
    maxTime=max(maxTime,d)
#for i in range(n+2):
  #if(distance[i]!=INF):
    #cnt+=1
    #if(distance[i]>maxTime):
      #maxTime=distance[i]

print(cnt-1,maxTime)

  




