n, m = map(int, input().split())
balls = list(map(int, input().split()))

#같은 무게를 고르면 안됨
count =0
# 처음부터 끝까지 인덱스마다
for i in range(len(balls)):
    # 현재 인덱스부터 끝까지 돌면서 현재와 다른 수가 있으면 count 추가
    for j in range(i+1, len(balls)):
        if balls[i] != balls[j]:
            count +=1
print(count)

######## 해답 #########
n, m = map(int, input().split())
data = list(map(int, input().split()))
array = [0]*11
# 해당 무게의 공이 몇개 있는지 저장
for x in data:
    array[x]+=1

result = 0
for i in range(1, m+1):
    n-=array[i] #무게가 i인 공의 개수 차감, 마지막에는 결국 0이 될 것
    result += array[i]*n # 한명은 i, 한명은 i가 아닌 공을 고르는 경우의 수 구해 더함

print(result)