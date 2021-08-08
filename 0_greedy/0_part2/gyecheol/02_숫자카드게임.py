# 2-3 그리디_숫자카드게임_조계철
import random

row,column = map(int,input("행과 열 크기 입력:").split()) #행,열 개수 입력
data = [[0]*column for _ in range(row)] # 2차원 배열 생성
for i in range(row):
    for j in range(column):
        data[i][j]=random.randint(1,10000)

print(data) # 소팅전 배열

res_list = []
for i in range(row):
    data[i].sort() # row별로 정렬
    res_list.append(data[i][0])
result = max(res_list)
#result = res_list.index(max(res_list))+1 # row를 출력할 경우 활용

print(data) # 소팅후 배열
print(result) # 정답


