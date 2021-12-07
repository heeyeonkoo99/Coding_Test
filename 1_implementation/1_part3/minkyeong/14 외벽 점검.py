from itertools import permutations

def solution(n, weak, dist):
    answer = 0
    length = len(weak) # 취약 지점 개수 저장
    
    # 원형 데이터를 직렬 데이터로 변경
    for i in range(length):
        weak.append(weak[i]+n)
    
    answer=len(dist)+1
    
    #0 ~ (취약지점개수) 순환하며 시작점 지정
    for start in range(length):
        # 친구의 순서 정함
        for friends in list(permutations(dist, len(dist))):
            count=1
            # friends가 start부터 점검 가능한 마지막 위치
            position = weak[start]+friends[count-1]
            # 지정된 시작점부터 취약지점 개수만큼 돌면서 확인
            for index in range(start, start+length):
                # friends가 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count +=1
                    # friends 투입이 불가하면 종료
                    if count>len(dist):
                        break
                    # 다음 friends가 점검 가능한 마지막 위치 저장
                    position=weak[index]+friends[count-1]
            # 투입할 친구 수의 최솟값 계산
            answer = min(answer, count)
    
    if answer>len(dist):
        return -1
    return answer