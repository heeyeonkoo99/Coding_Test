# Graph Algorithms


## Previous Concept 
- 그래프 자료구조
    - 개념: 노드와 노드 사이에 연결도니 간선의 정보를 갖고있는 자료구조
    - Graph: 방향/무방향, 순환/비순환, 루트 노드 없음, 부모 자식 관계 없음, 네트워크 모델

    - Tree: 방향, 비순환, 루트 노드 있음, 부모 자식 관계 있음, 계층 모델

- 그래프 구현 방법
    - 인접 행렬(Adjacency Matrix): 2차원 배열을 사용해 vertex간의 관계 저장, Floyd Warshall Algorithm에서 사용됨, O($V^2$) 공간 필요

    - 인접 리스트(Adjacency List):리스트를 사용해 edge의 정보 저장, Dijkstra Algorithm에서 사용됨, O($E$) 공간 필요

## 서로소 집합(Disjoint Sets)

서로소 집합: 공통 원소가 없는 두 집합

서로소 집합 자료구조: 서로소 부분 집합들로 나누어진 원소들의 데이터 처리를 위한 자료구조

-  O($V+M log_{2-M/V}V$)

- union: 2개의 원소가 포함된 집합을 하나의 집합으로 합침, 더 작은 번호를 가진 루트 노드가 큰 번호를 가진 루트 노드의 부모 노드가 됨

- find: 특정 원소가 속한 집합이 어떤 집합인지 찾음

```python
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a>b:
        parent[b]=a
    else:
        parent[a]=b

#vertex, edge 개수 각각 입력받기
v, e = map(int, input().split())

#부모 테이블 초기화
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i]=i

#입력받은 a,b값으로 union 진행
for i in range(e):
    a,b=map(int, input().split())
    union_parent(parent, a, b)

#각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
```

- 서로소 집합을 활용한 사이클 판별

노드 두개를 순서대로 union하면서 루트노드가 같지 않으면 사이클 없는 것, 루트노드가 같은 경우가 발생하면 사이클이 있는 것

```python
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#vertex, edge 개수 각각 입력받기
v, e = map(int, input().split())

#부모 테이블 초기화
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i]=i

#사이클 판별 시작
cycle = False

for i in range(e):
    a,b=map(int, input().split())
    if find_parent(a)==find_parent(b): #루트 노드가 같은 경우가 발생하면
        cycle = True #사이클 존재
        break
    else:
        union_parent(parent, a, b)

print(cycle)
```

## Kruskal Algorithms

- Spanning Tree (신장 트리): 모든 노드를 포함(연결)하면서 사이클이 존재하지 않는 부분 그래프

최소 비용으로 신장 트리를 만들 수 있는 알고리즘

그리디 알고리즘

- 가장 거리가 짧은 edge부터 차례대로 집합에 추가하면서 사이클 발생 여부를 확인한다

- O($E logE$)  *데이터 정렬에 필요한 시간

```python
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#vertex, edge 개수 각각 입력받기
v, e = map(int, input().split())

#부모 테이블 초기화
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i]=i

edges=[]
result = 0

#edge들에 대한 정보 입력받음
for i in range(e):
    a,b,cost=map(int, input().split())
    edges.append((cost, a, b)) #비용순으로 정렬하기 위해

edges.sort()

#edge 하나씩 추가하며 알고리즘 진행
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b): #루트 노드가 같지 않으면 사이클 없는 것
        union_parent(parent, a, b)
        result += cost

print(result)
```

## Topology Algorithms

방향 그래프의 모든 노드를 방향성에 맞게 순서대로 나열하는 것

- 진입 차수(Indegree): 특정한 노드로 들어오는 간선의 개수

- 진입 차수가 0인 노드를 큐에 넣은 후 해당 노드에서 출발하는 간선 제거
-> 새롭게 진입 차수가 0이 된 노드 큐에 넣고 반복

- O($V+E$) *vertex와 edge를 모두 확인
```python
from collections import deque
v, e = map(int, input().split()) #vertex, edge 개수 입력
indegree = [0]*(v+1) #노드별 진입 차수 저장
graph = [[]for i in range(v+1)] #노드별 edge 정보 저장

for i in range(e):
    a, b = map(int, input().split())
    indegree[b]+=1
    graph[a].append(b)

def topology_sort():
    q = deque()
    result = []
    for i in range(v+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now) #현재 원소를 저장
        for elem in graph[now]:
            indegree[elem]-=1
            if indegree[elem]==0:
                q.append(elem)
    
    print(result)
topology_sort()

```
