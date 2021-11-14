p = list(input())
x = int(p[1])
y = int(ord(p[0])) - int(ord('a'))+1

move = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

count = 0
for m in move:
    mx = x+m[0]
    my = y+m[1]
    # 범위 벗어나면 제외
    if mx<1 or my<1 or mx>8 or my>8:
        continue
    count +=1
print(count)