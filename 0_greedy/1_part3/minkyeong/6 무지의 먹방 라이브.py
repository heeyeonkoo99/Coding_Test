import heapq
def solution(food_times, k):
    # 전체 음식 먹는 시간보다 k가 크거나 같으면 -1 반환
    if sum(food_times)<=k:
        return -1
    
    # 시간이 적은 음식부터 빼기 위해 우선순위큐 사용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1)) #먹는 시간, 음식 번호 저장
    
    # 먹기 위해 사용한 시간, 직전에 다 먹은 음식 시간, 남은 음식 개수 선언
    sum_value = 0
    previous = 0
    length = len(food_times)
    
    #sum_value + ((현재 음식 시간-이전 음식시간) * 음식 개수)
    while sum_value+((q[0][0]-previous)*length)<=k:
        now = heapq.heappop(q)[0] # 가장 짧은 음식 시간
        sum_value+=(now-previous)*length # 한바퀴 도는 것
        length -=1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
    
    # k초 이후 남은 음식들만 q에 남게 됨
    # 음식의 번호 기준으로 정렬
    # 남은 시간(k-sum_value)을 남은 음식 개수로 나눈 후 얻어진 나머지값의 번호 반환
    
    result = sorted(q, key=lambda x:x[1])
    return result[(k-sum_value)%length][1]