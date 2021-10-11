# 집 개수, 마을 개수
n, m = map(int, input().split())

#edge 저장할 리스트 생성
edges = []

#원소 별 루트 노드 저장하는 배열 선언
parent = [0]*(n+1)
for i in range(n+1):
    parent[i]=i

#최소 비용 저장할 변수
result = 0

#루트노드 찾기
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

#두 집을 한 마을으로 합친다
def union(a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# a,b를 연결하는 노드의 비용:c
for i in range(m):
    a,b,cost=map(int, input().split())
    edges.append((cost, a, b))

#가장 작은 비용부터 사용하기 위해 정렬
edges.sort()

max_cost=0
for edge in edges:
    cost, a,b = edge
    if find_parent(parent, a)!=find_parent(parent, b):
        union(a,b)
        max_cost = max(cost, max_cost) #가장 큰 값을 구하는 것
        #last = cost -> 어차피 정렬된 데이터이므로 이렇게 큰 값 구할 수 있음
        result +=cost

# 일단 최소 신장 트리를 만들어 최소 비용을 구한 후, 
# 가장 큰 비용을 가진 노드 하나를 없애면
# 마을 두개를 가진 최소 비용을 찾을 수 있다!
print(result-max_cost)