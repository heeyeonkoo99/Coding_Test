#모험가 길드
n=int(input())
fear=list(map(int, input().split()))
fear.sort(reverse=True) #내림차순으로 sorting

groupNum=0;

i=0
while i<n :
    groupNum=groupNum+1
    i=i+fear[i]
print(groupNum)





