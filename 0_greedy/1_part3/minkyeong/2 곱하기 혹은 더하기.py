l = list(input())
l = [int(i) for i in l]
print(l)
total = 0
# 예제와 비슷하지만 리스트의 원소를 하나씩 지워나가는 방식
while l:
    now = l[0]
    if now in (0,1) or total in(0,1):
        total += now
    else:
        total *= now
    l.pop(0)
print(total)