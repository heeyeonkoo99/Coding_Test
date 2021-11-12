# 무지의 먹방 라이브
import heapq
def solution(food_times, k):
    if sum(food_times)<=k : # 0, 0, 0, ... ,0인 상태
        return -1
    q=[]
    for i in range(len(food_times)) :
        heapq.heappush(q,food_times[i],i+1)

    time=0
    previous=0
    food_len=len(food_times)
    while time+(q[0][0]-previous)*food_len <=k:
        now=heapq.heappop(q)[0]
        time+=(now-previous)*food_len
        length-=1
        previous=now

    res=sorted(q,key=lambda x:x[1])
    return res[(k-time)%food_len][1]




    return answer


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
