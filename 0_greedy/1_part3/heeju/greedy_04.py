n=int(input())
coin_list=list(map(int,input().split()))
coin_list.sort() #11239

target=1
for i in coin_list :
    if target<i :
        break
    target+=i

print(target)


