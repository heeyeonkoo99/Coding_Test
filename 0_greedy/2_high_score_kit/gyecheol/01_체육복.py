# kit_01 그리디_체육복_조계철
def solution(n, lost, reserve):
    answer = 0
    borrow_cnt = 0  # 체육복을 빌려준 횟수
    lost.sort()
    reserve.sort()
    lost_students = []  # 체육복을 잃어버렸는데 자신을 위한 여벌의 체육복도 있는 학생 리스트
    lost_length = len(lost)

    for i in range(len(lost)):
        if lost[i] in reserve:  # 체육복을 잃어버렸는데 자신을 위한 여벌의 체육복이 있다면
            lost_students.append(lost[i])
            reserve.remove(lost[i])
            borrow_cnt += 1
    for student in lost_students:  # 체육복을 잃어버렸는데 자신을 위한 여벌의 체육복이 있는 학생을 lost리스트에서 제외
        lost.remove(student)

    for i in range(len(lost)):
        if lost[i] - 1 in reserve:
            reserve.remove(lost[i] - 1)
            borrow_cnt += 1
        elif lost[i] + 1 in reserve:
            reserve.remove(lost[i] + 1)
            borrow_cnt += 1
        else:
            continue

    answer = n - lost_length + borrow_cnt
    return answer

# 당장 좋은 것을 선택한다는 그리디의 의미가 이번 문제에서 잘 드러난 것 같다