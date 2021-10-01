n = int(input())
d = [0]*n

d[0]=1 #1을 채우는 경우의 수
d[1]=3 #2를 채우는 경우의 수

for i in range(2, n):
    d[i]= d[i-1]+d[i-2]*2
print(d[n-1])