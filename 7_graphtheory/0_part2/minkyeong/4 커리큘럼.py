from collections import deque
import copy

#듣고자 하는 강의 개수
n = int(input())
indegree = [0]*(n+1) #진입 차수 저장하는 배열
lec_len = [0]*(n+1) #강의별 소요되는 시간
graph = [[] for _ in range(n+1)]

for i in range(1,n+1): # n줄만큼 강의에 대한 정보 저장
    inp = list(map(int, input().split()))
    lec_len[i] = inp[0] #첫번째 인수는 i번째 강의의 시간
    for x in inp[1:-1]: #i번째 강의를 듣기 위해 여러개의 강의가 필요할 수 있으므로 for문 돌려서 하나씩 처리
        #x -> i : i를 듣기 위해선 x를 먼저 들어야 함
        indegree[i]+=1 #i로 들어오는 진입차수 추가
        graph[x].append(i) # x번째 배열에 i를 추가 -> queue에서 꺼낼 때 진입차수가 적은 x번째 배열에서 뻗어나갈 수 있도록 함

print(graph)

def topology_sort():
    result = copy.deepcopy(lec_len) #자기 자신의 걸리는 시간 저장
    q = deque()

    for i in range(1, n+1):
        if indegree[i]==0: #진입차수 0인 노드들을 q에 저장
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]: #현재 노드로 진입하는 노드들에 대해
            result[i]=max(result[i], result[now]+lec_len[i]) # 기존 i의 강의시간과 (현재노드의 강의시간+i의 강의시간) 중 큰 값 저장
            indegree[i]-=1 #now 강의를 들은 시간까지 합쳐 result[i]에 저장했으므로, 진입노드중 now를 삭제
            if indegree[i]==0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()