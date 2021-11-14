l = list(input())
l = [int(i) for i in l]

#왼쪽 반의 합과 오른쪽 반의 합이 같으면
if sum(l[:len(l)//2])==sum(l[len(l)//2:]):
    print("LUCKY")
else:
    print("READY")