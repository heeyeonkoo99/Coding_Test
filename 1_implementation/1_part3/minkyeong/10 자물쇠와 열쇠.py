def rotate(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j]!=1:
                return False
    return True
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    # lock을 3배로 늘린 이차원 배열 생성
    new_lock = [[0]* (n*3) for _ in range(n*3)]
    #new_lock의 가운데에 lock의 데이터 입력
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        # key를 회전하면서
        key = rotate(key)
        # (x,y)는 key의 왼쪽위 시작점을 의미
        # (0,0) 부터 (n*2, n*2)부분까지만 탐색하여 자물쇠가 열쇠와 맞는지 확인 
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠 적용 후 new_lock 업데이트
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+= key[i][j]
                # 자물쇠 테스트
                if check(new_lock)==True:
                    return True
                # 연산 리셋
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
    return False