n, m=map(int, input().split())
lengs = list(map(int, input().split()))

#이진탐색 적용 x
# height = max(lengs)
# while True:
#     result = [x-height if x-height>0 else 0 for x in lengs]
#     if sum(result) < m:
#         height -= 1
#     else:
#         print(height)
#         break

#이진탐색 적용 o
def find(lengs, m, start, end):
    while start <= end:
        mid = (start+end)//2
        result = [x-mid if x-mid>0 else 0 for x in lengs]
        total = sum(result)
        if total > m:
            start = mid+1
        elif total < m:
            end = mid -1 #끝점을 감소시키면 중간점도 감소되어 sum(result)값을 키우게 되는 원리
        else:
            return mid

print(find(lengs, m, 0, max(lengs)))