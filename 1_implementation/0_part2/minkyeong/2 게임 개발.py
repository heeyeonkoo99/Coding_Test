def main():
    #nxm 맵
    n,m = map(int, input().split())

    # 방문 여부 저장하는 이차원 리스트
    # 방문하면 1로, 방문하지 않으면 0으로 처리
    d = [[0]*m for _ in range(n)]

    #유저 위치와 방향
    x,y,direction = map(int, input().split())
    d[x][y]=1
    
    # 게임 맵 저장하는 이차원 리스트
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))

    #direction에 따라 이동하는 좌표를 설정
    # 북, 동, 남, 서 순으로 이동할 수 있도록 함
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    count = 1
    turn_time=0

    #시뮬레이션 시작
    while True:
        # 왼쪽으로 회전
        direction = turn_left(direction)
        # 회전 후 이동하려는 좌표
        nx = x+dx[direction]
        ny = x+dy[direction]

        #이동하려는 좌표가 유효하면 방문 처리
        if d[nx][ny]==0 and array[nx][ny]==0:
            d[nx][ny]=1
            x=nx
            y=ny
            count +=1
            turn_time=0
            continue
        else: #이동하려는 좌표가 유효하지 않으면 회전 카운트
            turn_time +=1
        
        # 4번 회전했는데 이동을 못하면
        if turn_time ==4:
            # 같은 방향의 뒤쪽으로 이동하려는 좌표
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 이동하는 좌표가 바다가 아니라면 뒤로 이동
            if array[nx][ny]==0:
                x = nx
                y = ny
                count +=1
            else: #뒤로 이동할 수 없을 때 -> 시뮬레이션 중단
                break
            turn_time=0

    print(count)

# 왼쪽으로 방향 회전
def turn_left(direction):
    direction-=1
    if direction==-1:
        direction=3
    return direction

if __name__=="__main__":
    main()