# 구현_3_07_럭키스트레이트

score = input("점수:")
f_score = 0
b_score = 0
half_length = int(len(score)/2)

for i in range(0,half_length):
    f_score += int(score[i])
for i in range(half_length,len(score)):
    b_score += int(score[i])
if f_score == b_score:
    print('LUCKY')
else:
    print("READY")
