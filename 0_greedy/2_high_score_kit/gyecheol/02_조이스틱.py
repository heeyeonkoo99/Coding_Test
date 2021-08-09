# kit_02 그리디_조이스틱_조계철
def solution(name):
    orderly_a_cnt = 0  # 순행방향으로 두번째 문자부터 연속된 A 카운트
    reverse_a_cnt = 0  # 역행방향으로 마지막 문자부터 연속된 A 카운트
    a_cnt = 0  # 전체 A 카운트
    answer = 0  # 조이스틱 조작 횟수
    # abcde
    # fghij
    # klm
    # nopqr
    # stuvw
    # xyz

    for i in range(1, len(name), 1):  # 순행방향 연속된 A 카운트
        if name[i] == 'A':
            orderly_a_cnt += 1
        else:
            break;

    for i in range(len(name) - 1, 0, -1):  # 역행방향 연속된 A 카운트
        if name[i] == 'A':
            reverse_a_cnt += 1
        else:
            break;


    answer += (len(name) - 1 - max(orderly_a_cnt, reverse_a_cnt))

    for i in range(len(name)):
        if 'A' <= name[i] and name[i] <= 'M':
            answer += ord(name[i]) - ord('A')
        else:
            answer += ord('Z') - ord(name[i]) + 1

    if (orderly_a_cnt + 1) == len(name):  # 모두 A인 경우 고려
        answer = 0

    return answer


# 테스트케이스 11번 통과 못함... ex) ABAAAAAAAAABB 같이 한쪽 방향으로 가는 것이 아니라 양쪽으로 움직일때... 아이디어 추가 필요