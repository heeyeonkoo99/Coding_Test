# 2-2 그리디_큰수의법칙_조계철

n,m,k = map(int,input("n,m,k를 입력:").split())
data = list(map(int,input("데이터 리스트 입력:").split()))
result=0

data.sort()

cnt = m // (k+1)
rmd = m % (k+1)
result = (data[-1]*k + data[-2])*cnt + (data[-1]*rmd)

print(result)


'''
결과적으로 이렇게 m과 k를 비교할 필요 없음
if m==k:
    result = data[-1]*k
else: # m!=k인 경우에는 m>k 이므로
    cnt = m // (k+1)
    rmd = m % (k+1)
    result = (data[-1]*k + data[-2])*cnt + (data[-1]*rmd)
'''