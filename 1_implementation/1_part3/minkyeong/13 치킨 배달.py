from itertools import combinations

N, M = map(int, input().split())
houses = []
chickens = []

for i in range(1, N+1):
    l = list(input().split())
    for j in range(1, len(l)+1):
        if l[j-1] =='1':
            houses.append((i,j))
        elif l[j-1]=='2':
            chickens.append((i,j))

#치킨집 중 m개를 고른 조합 결과를 리스트에 저장
chosen_chicken = list(combinations(chickens, M))

# 치킨 거리의 합 계산
def get_sum(chickens):
    result = 0
    for hx, hy in houses:
        road = 1e9
        for cx, cy in chickens:
            road = min(road, abs(hx-cx)+abs(hy-cy))
        result += road # 집에서 가장 가까운 치킨거리를 추가
    return result

result = 1e9
for i in chosen_chicken: 
    result = min(result, get_sum(i))

print(result)