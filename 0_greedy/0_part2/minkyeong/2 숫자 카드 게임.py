n,m = map(int, input().split())

max_min = 0
for i in range(n):
    l = list(map(int, input().split()))
    max_min = max(min(l),max_min)

print(max_min)