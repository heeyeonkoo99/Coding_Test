n = int(input())

l = list(map(int, input().split()))
'''
l.sort(reverse=True) # 내림차순으로 정렬
group = 0
# l에 원소들이 있을때까지
while l:
    # 가장 큰 첫번째 원소 가져옴
    now = l[0]
    # 첫번째 원소만큼 리스트에서 꺼내 그룹을 만들기 위해 체크
    if now <= len(l):
        l = l[now:] # 그룹이 된 원소들은 리스트에서 꺼냄
        group +=1 # 그룹 추가
    else: # 첫번째 원소의 길이만큼 리스트가 남아있지 않다면
        if now ==1: # 만약 첫번째 원소가 1이면 혼자서도 구성 가능
            group +=1 # 그룹 추가
        l.pop(0) # 첫번째 원소가 1이 아니면 그냥 삭제

print(group)
'''

######### 해답 #########

l.sort() #오름차순으로 정렬 -> 내림차순보다 많은 그룹을 생성할 수 있다
count = 0 # 그룹의 인원을 저장하여 공포도와 비교
result = 0 # 생성된 그룹 개수 저장
for i in l:
    count +=1
    if count>=i: # 현재 공포도보다 인원수가 많으면
        result +=1 # 그룹 하나 생성
        count = 0
print(result)