from collections import deque
import copy

n=int(input())

indegree=[0]*(n+1)
graph=[[]for i in range(n+1)]
time=[0]*(n+1)

for i in range(1,n+1):
  data=list(map(int,input().split()))
  time[i]=data[0]
  for j in range(1,len(data)-1):
    indegree[i]+=1
    graph[data[j]].append(i)


def topoloty_sort():
  result=copy.deepcopy(time)
  q=deque()

  for i in range(1,n+1):
    if(indegree[i]==0):
      q.append(i)
  
  while q:
    temp=q.popleft()
    for i in graph[temp]:
      result[i]=max(result[i],result[temp]+time[i])
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)

  for i in range(1,n+1):
    print(result[i])

topoloty_sort()


