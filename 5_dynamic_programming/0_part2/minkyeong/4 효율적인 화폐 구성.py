price = []
n, m = map(int, input().split())
for i in range(n):
    price.append(int(input()))

#n번째 element를 만들기 위해 필요한 화폐의 최소 개수 저장
d = [10001]*(m+1)
d[0]=0 #0원을 만들기 위해 필요한 화폐의 개수는 0개
for i in range(n): #price 내의 화폐들을 돌면서
    for j in range(price[i], m+1):
            if d[j-price[i]]!=10001: # 현재 인덱스에서 화폐 한 개 뺀 인덱스의 값이 존재하면
                d[j]=min(d[j], d[j-price[i]]+1) # 현재개수와, (화폐 한개뺀 값+화폐값)의 화폐 개수 비교해서 작은 값 사용
    print(d)

if d[m]==10001:
    print(-1)
else:
    print(d[m])