# 3-4 그리디_만들수없는금액_조계철
n = int(input("동전의 개수:"))
currency = list(map(int,input("화폐 단위 입력:").split()))
idx=0

currency.sort()


################################ 4번 일단 보류
