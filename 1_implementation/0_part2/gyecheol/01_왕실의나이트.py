# 구현_2_01_왕실의나이트_조계철

location = input("나이트의 현재 위치:")

cnt = 0

if (ord(location[0]) - ord('a') == 0) or (ord('h') - ord(location[0]) == 0): # 좌우 방향 중 한쪽방향으로 1칸 이동이 불가하다면
    cnt += 2
elif (ord(location[0]) - ord('a') == 1) or (ord('h') - ord(location[0]) == 1):  # 좌우 방향 중 한쪽방향으로 2칸 이동이 불가하다면
    cnt += 1
else:
    pass


if (int(location[1]) - 1 == 0) or (9 - int(location[1]) == 0): # 상하 방향 중 한쪽방향으로 1칸 이동이 불가하다면
    cnt += 2
elif (int(location[1]) - 1 == 1) or (9 - int(location[1]) == 1):  # 좌우 방향 중 한쪽방향으로 2칸 이동이 불가하다면
    cnt += 1
else:
    pass


if cnt == 4:
    result = 2
elif cnt == 3:
    result = 3
elif cnt == 2:
    result = 4
elif cnt == 1:
    result = 7
else:
    result = 8

print(result)