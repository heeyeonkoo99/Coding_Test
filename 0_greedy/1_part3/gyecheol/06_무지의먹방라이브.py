# 3-5 그리디_무지의먹방라이브_조계철

def solution(food_times, k):
    c_time = 0  # current_time: 현재까지 걸린 시간
    c_idx = 0  # current_idx: 현재까지 옮겨간 인덱스
    food_length = len(food_times)
    sum_times = 0

    for value in food_times:
        sum_times += value

    if sum_times <= k:
        answer = -1
    else:
        while c_time != k:
            idx = c_idx % food_length
            if food_times[idx] != 0:
                food_times[idx] -= 1
                c_time += 1
                c_idx += 1
            else:
                c_idx += 1
        if c_time == k:
            idx = c_idx % food_length
            while food_times[idx] == 0:
                c_idx += 1
                idx = c_idx % food_length
        answer = idx + 1
    return answer


# 정확도 테스트: all 통과
# 효율성 테스트: 0점..