#곱하기 혹은 더하기
import sys
s=sys.stdin.readline().rstrip() #input은 입력 속도가 느리기 때문에 사용한다.
numList=list(map(int, s))
numList.sort(reverse=True)

res=numList[0]
for i in range(1, len(numList)) :
    if numList[i]!=0 :
        res*=numList[i]
print(res)



