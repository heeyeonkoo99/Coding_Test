def solution(people, limit):
    answer = 0
    sum = 0
    people_length = len(people)
    idx = 0
    c_idx = 0
    people.sort()

    while c_idx != people_length:
        if idx == people_length:
            answer += 1
            break;
        sum += people[idx]
        idx += 1
        if sum > limit:
            answer += 1
            idx -= 1
            sum = 0
            c_idx = idx
        elif sum == limit:
            answer += 1
            sum = 0
            c_idx = idx

    return answer

### 실패... 순서대로 태우려고 했는데 그러면 안됐다
## 희연이꺼(답지) 봤는데, 더 좋은 풀이를 찾기 힘들어서 푼 데까지만 올림