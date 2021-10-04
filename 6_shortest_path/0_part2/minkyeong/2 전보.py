import sys
import heapq

#도시, 통로의 개수 입력이 크므로 플로이드보다는 dijkstra 사용하는게 나음
INF = int(1e9)
input = sys.stdin.readline


#n: 도시 개수, m: 통로 개수, c: 메시지 보내고자 하는 도시
n, m, city= map(int, input().split())

# 도시마다 연결된 통로, 비용의 쌍을 저장하는 배열
graph = [[] for _ in range(n+1)]

#최소 비용 저장하는 배열
distance = [INF]*(n+1)

for i in range(m):
    f, t, cost = map(int, input().split())
    graph[f].append((t, cost))

#distance 배열을 dijkstra 알고리즘으로 계산하여 채움
def dijkstra(city):
    #우선순위 큐
    q = []
    heapq.heappush(q, (0, city))
    distance[city]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(city)
city_cnt = 0 # start city에서 접근 가능한 도시 개수
max_time = 0 # 특정 도시로의 최고 비용이 총 시간이 될 것(동시에 다른 도시로 전보가 전달되므로)

for i in distance:
    if i != INF and i !=0:
        city_cnt +=1
        max_time = max(max_time, i)
print(city_cnt, max_time)