import math
# 문자가 모두 같도록
# 연속된 하나이상의 숫자를 0<->1 변환
l = list(input())
l = [int(i) for i in l]
# 숫자가 바뀌는 시점 count
count = 0
for i in range(len(l)-1):
    if l[i] != l[i+1]:
        count +=1
# 반으로 나눠주면 바꾸는 경우의 수 구할 수 있음
print(math.ceil(count/2))

######### 해답 #########
#0으로 만드는 경우와 1로 만드는 경우 중 적게 걸리는 경우를 택함
count0=0
count1=0
data = input()
if l[0]=='1':
    count0+=1
else:
    count1+=1

for i in range(len(data)-1):
    if data[i]!=data[i+1]:
        if data[i+1]=='1':
            count0+=1
        else:
            count1+=1
print(min(count0, count1))