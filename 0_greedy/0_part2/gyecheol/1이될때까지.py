# 2-4 그리디_1이될때까지_조계철
n,k = map(int,input("n과 k를 입력:").split())
cnt=0 # 수행 횟수
while n!=1:
    if n % k ==0:
        n /= k
        cnt+=1
    else:
        n-=1
        cnt+=1
print(cnt)