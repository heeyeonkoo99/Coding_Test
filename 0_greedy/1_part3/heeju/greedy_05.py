#볼링공 고르기
n,m=map(int,input().split())
balls=list(map(int,input().split()))
ball_count=[0]*11

res=0
for i in balls :
    ball_count[i]+=1

for i in range(1,m+1):
    n-=ball_count[i]
    res+=n*ball_count[i]

print(res)

