# 3-1 그리디_모험가길드_조계철
n = int(input("모험가의 수 n값:"))
data = list(map(int,input("모험가들의 공포도 입력:").split()))

data.sort()
cnt=0 # 그룹 개수
idx=0
length = len(data)
print(data)
while length>0: #그룹 지을 모험가가 더이상 남아 있지 않을때까지
    if (length // data[idx]) >= 1: #공포도에 맞는 인원수가 남아 있다면
        cnt+=1
        length-=data[idx]
        idx+=data[idx]
    else:
        break

print(cnt)