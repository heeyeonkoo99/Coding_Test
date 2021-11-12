#문자열 뒤집기
import sys
s = sys.stdin.readline().rstrip()
listS = list(map(int, s))

cNum = 0
flag=listS[0]
for i in listS:
    if i != flag:
        cNum += 1
        flag=i

res= int(cNum/2) if (cNum%2==0) else int(cNum/2)+1
print(res)
