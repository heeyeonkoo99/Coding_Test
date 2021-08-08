# 3-2 그리디_곱하기혹은더하기_조계철
n = input("입력값:")
zero_cnt=0 # 입력받은 문자열에서 0이 아닌 문자가 나올때까지 문자개수
result=0

for i in range(len(n)):
    if n[i]=='0':
        zero_cnt+=1 # 시작부터 0이 아닌 숫자가 나올때까지 카운트
    else:
        break; #0이 아닌 문자가 나오는 순간 break

result+=int(n[zero_cnt])

for i in range(zero_cnt+1,len(n)):
    if n[i]=='0' or n[i]=='1':
        result+=int(n[i])
    else:
        result*=int(n[i])

print(result)