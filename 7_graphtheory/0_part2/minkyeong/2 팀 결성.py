n, m = map(int,input().split())

parent = [0]*(n+1)

for i in range(n+1):
    parent[i]=i

def find_parent(parent, a):
    if parent[a]!=a:
        #경로 압축 방식으로 사용해야 큰 범위 커버 가능
        parent[a]=find_parent(parent, parent[a])
        #return find_parent(parent, parent[a])
    return parent[a]

def union(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(m):
    arg, a, b = map(int, input().split())
    if arg==0:
        union(a,b)
    elif arg ==1:
        if find_parent(parent, a)==find_parent(parent, b):
            print("YES")
        else:
            print("NO")
        # if a<b:
        #     if find_parent(parent, b)==a:
        #         print("YES")
        #     else:
        #         print("NO")
        # else:
        #     if find_parent(parent, a)==b:
        #         print("YES")
        #     else:
        #         print("NO")
