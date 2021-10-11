from collections import deque
import copy

#듣고자 하는 강의 개수
n = int(input())
indegree = [0]*(n+1)
lec_len = [0]*(n+1)
graph = [[] for _ in range(n+1)]

print(graph)
for i in range(1,n+1):
    inp = list(map(int, input().split()))
    lec_len[i] = inp[0]
    for x in inp[1:-1]:
        indegree[x]+=1 #x로 들어오는 노드 개수에 추가
        graph[x].append(i) #x로 들어오는 노드 배열에 i를 추가


def topology_sort():
    result = copy.deepcopy(lec_len)
    q = deque()

    for i in range(1, n+1):
        if indegree[i]==0: #진입차수 0인 노드들을 q에 저장
            q.append(i)
    print(q)
    while q:
        now = q.popleft()
        for i in graph[now]: #현재 노드로 진입하는 노드들에 대해
            result[i]=max(result[i], result[now]+lec_len[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()