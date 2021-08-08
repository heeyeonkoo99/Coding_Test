# 3-4 그리디_볼링공고르기_조계철
n = int(input("볼링공 개수:"))
m = int(input("공의 최대무게:"))
balls = list(map(int,input("공 무게 입력:").split()))
cnt=0


for i in range(len(balls)):
    for j in range(i,len(balls)):
        if balls[i] != balls[j]:
            cnt+=1

result= cnt
print(result)