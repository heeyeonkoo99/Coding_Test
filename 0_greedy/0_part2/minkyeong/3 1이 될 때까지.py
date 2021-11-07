n, k = map(int, input().split())

count = 0
'''
while n >= k:
    #나누어 떨어질 때 까지 1을 뺌
    while n%k !=0:
        n-=1
    # 나누어 떨어지면 나누기
    n //= k
    count +=1
# k보다 작아져 나머지 값이 나왔으면 1 빼주기
while n>1:
    n-=1
    count +=1
print(count)
'''

# 효율적으로 계산하기

while True:
    target = (n//k) *k
    # k로 나누어떨어지는 수까지 1 빼기 count
    count += (n-target)
    n = target
    if n < k:
        break
    # k로 나누는 것 count
    count += 1
    n//=k
# k보다 작은 나머지 수 하나씩 빼기 count
count +=(n-1)
print(count)