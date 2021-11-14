def solution(s):
    res_by_len = [len(s)]*len(s)
    # 문자열 s를 i개씩 잘라 결과 문자열이 가장 짧을 때의 n값을 반환
    for i in range(1, len(s)):
        components = []
        # 문자열 s에서 맨 처음 n개 저장
        components.append(s[0:i])
        count = 1 # 연속해서 같은 수가 나올 때 개수 증가
        result = '' # 결과 문자열 저장
        # 문자열 s를 i개씩 자르면서
        for j in range(i, len(s), i):
            #이전것과 같으면
            if components[-1] == s[j:j+i]:
                count +=1
                components.append(s[j:j+i]) #현재 값 추가
            else:# 이전것과 같지 않으면 (이전 카운트 + 이전 값)을 결과 문자열에 추가
                #이전 카운트가 2 이상일때만 카운트 개수 추가
                if count>1:
                    result +=str(count)
                result +=components[-1] # 이전 값
                count =1
                components.append(s[j:j+i]) #현재 값 추가
        if count>1:
            result +=str(count)
        result +=components[-1]
        res_by_len[i]=len(result)
    
    return min(res_by_len)