def possible(answer):
    for x, y, stuff in answer: # 모든 구조물 검사
        if stuff ==0: # 기둥이라면
            if y==0 or [x-1, y, 1] in answer or [x, y, 1] in  answer or [x, y-1, 0] in answer:
                # 바닥 위/ 보의 한쪽 끝 위/ 다른 기둥 위 라면 조건 충족
                continue
            return False
        elif stuff==1: # 보라면
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                # 왼쪽 끝부분에 기둥/ 오른쪽 끝에 기둥/ 양쪽에 보 라면 조건 충족
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate==0: # 제거하는 경우
            answer.remove([x, y, stuff]) # 먼저 제거해보고
            if not possible(answer): #조건 미충족 시 다시 추가
                answer.append([x, y, stuff])
        if operate==1: # 입력하는 경우
            answer.append([x, y, stuff]) # 먼저 입력해보고
            if not possible(answer): # 조건 미충족시 삭제
                answer.remove([x, y, stuff])
    return sorted(answer)
            



# 내가 구현한 것 -> 테스트케이스 통과 실패

# def f_check(x,y, answer):
#     if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer: #conditions
#         return True
#     elif [x-1, y, 1] in answer and [x+1, y, 1] in answer: #conditions
#         return True
#     return False

# def solution(n, build_frame):
#     answer = []
#     for i in build_frame:
#         if i[3]==0: # 삭제할 경우
#             if i[2]==0: #기둥 삭제 시
#                 # 보 체크
#                 check = False
#                 if [i[0],i[1]+1,1] in answer:
#                     if f_check(i[0],i[1]+1, answer):
#                         check = True
#                 if [i[0]-1,i[1],1] in answer:
#                     if f_check(i[0],i[1]+1, answer):
#                         check = True
#                 if check:
#                     answer.remove([i[0],i[1],0])
#             else: #보 삭제 시
#                 # 양옆의 보 조건 확인
#                 if not (f_check(i[0]-1, i[1], answer) and f_check(i[0]+1, i[1], answer)):
#                     answer.remove([i[0],i[1],1])
#         else: # 설치할 경우
#             if i[2]==0: # 기둥 설치 시
#                 if i[0]>=0 and i[0]<=n and i[1]>=0 and i[1]<n: #범위체크
#                     if i[1]!=0:
#                         if [i[0], i[1]-1, 0] in answer or [i[0]-1, i[1], 1]  in answer: #conditions
#                             answer.append([i[0], i[1], i[2]]) # 기둥 설치
#                     else: # 바닥이면 기둥 설치
#                         answer.append([i[0], i[1], i[2]])
#             else: # 보 설치 시
#                 if i[0]>=0 and i[0]<n and i[1]>0 and i[1]<=n: #범위체크
#                     if f_check(i[0], i[1], answer):
#                         answer.append([i[0], i[1], i[2]])
#     return sorted(answer)