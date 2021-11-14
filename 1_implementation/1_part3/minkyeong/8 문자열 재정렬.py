l = list(input())
ch=[]
num=[]
for i in l:
    #아스키 코드가 65 이상 -> 알파벳 대문자이면
    if ord(i)>=65:
        # char 배열에 추가
        ch.append(ord(i))
    # 숫자라면
    else:
        # num 배열에 int로 형변환하여 추가
        num.append(int(i))

# 알파벳은 정렬을 해준다
ch.sort()
result = ''

# 알파벳을 하나씩 결과 문자열에 추가
for i in ch:
    result += chr(i)

# 숫자의 합 추가
result += str(sum(num))
print(result)

########### 해답 코드 #############
data = input()
result = []
value = 0

for x in data:
    # 알파벳인지 판별 -> isalpha
    if x.isalpha():
        result.append(x)
    # 숫자는 합함
    else:
        value+=int(x)

result.sort()

if value !=0: #합한 숫자 더함
    result.append(str(value))
print(''.join(result))