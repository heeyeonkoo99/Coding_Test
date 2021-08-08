# 3-3 그리디_문자열뒤집기_조계철
n = input("입력값:")
zero_group_cnt=0 # 0의 무리
one_group_cnt=0 # 1의 무리
current_value= n[0]

if n[0]=='0': # 첫 문자가 0이라면
    zero_group_cnt=1
else:
    one_group_cnt=1

for i in range(len(n)):
    if n[i] != current_value: # 0과 1이 서로 바뀌는 순간
        if current_value=='0': # 0에서 1로 바뀐다면
            one_group_cnt+=1
        else:                   #1에서 0으로 바뀐다면
            zero_group_cnt+=1
        current_value=n[i] # 바뀌면 현재 값을 다시 저장

if one_group_cnt>=zero_group_cnt: # 1그룹 개수가 더 많거나 같으면
    result=zero_group_cnt
else:
    result=one_group_cnt #입력값이 0이나 1, 또는 00, 11이라도 가능한 솔루션

print(result)

