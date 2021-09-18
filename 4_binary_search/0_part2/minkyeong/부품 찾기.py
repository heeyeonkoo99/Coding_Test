import sys
n = int(input())
stock = []
res = []

def find(stock, item, start, end):
    while start<=end:
        mid = (start+end)//2
        if stock[mid] == item:
            return mid
        elif stock[mid]<item:
            start = mid +1
        elif stock[mid]>item:
            end = mid-1
    return None

line = sys.stdin.readline().rstrip()
for i in range(n):
    stock.append(int(line.split()[i]))

m = int(input())
line = sys.stdin.readline().rstrip()
for i in range(m):
    res.append(int(line.split()[i]))

#이진탐색을 위해 정렬
stock.sort()

for i in res:
    #이진탐색
    result = find(stock, i, 0, len(stock)-1)
    if result is None:
        print("no", end=" ")
    else:
        print("yes", end=" ")