def main():
    n,m,k = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    total = 0

    '''
    # 최대 k번 연속 가능
    # m번 더함
    iter = 0   
    
    # 예제와 달리 iter값을 더해가는 방식
    # 예제처럼 m을 감소시키는 것이 메모리 차원에서 더 좋음
    while True:
        for i in range(k):
            if iter >= m:
                break
            else:
                total += numbers[-1]
                iter +=1
        if iter >= m:
                break
        else:
            total += numbers[-2]
            iter +=1
    '''
    # k+1 -> 가장 큰 수 k번, 두번째로 큰 수 1번 더한다는 의미
    # m개 중 k+1을 사용할 수 있는 경우 -> 가장 큰 수를 k번 더할 수 있는 경우의 수
    count = int(m/(k+1))*k 
    # m개 중 k+1으로 나눈 후 나머지의 경우 -> 가장 큰 수를 나머지만큼 더할 수 있음
    count += m%(k+1)

    total += count*numbers[-1]
    total += (m-count)*numbers[-2]

    print(total)

if __name__=="__main__":
    main()