n= int(input())
move = list(input().split())

#L R U D 순서로 저장
mx=[0, 0, -1, 1]
my=[-1, 1, 0, 0]
directions=['L','R','U','D']

x, y = 1, 1
for m in move:
    for i in range(len(directions)):
        if m == directions[i]:
            nx = x+ mx[i]
            ny = y+ my[i]
    # 이동 후 좌표가 범위를 벗어나면 다음 move로
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    # 이동 후 좌표가 범위 내이면 move 갱신
    x, y = nx, ny

print(x,y)