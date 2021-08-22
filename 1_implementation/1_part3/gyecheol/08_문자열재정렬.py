# 구현_3_08_문자열재정렬
input_string = input("문자열:")
# ord('0') == 48
# ord('9') == 57
data = list(input_string)
data.sort()

for i in range(len(data)):
    if ord(data[i])>=48 and ord(data[i])<=57: # 숫자라면
        continue
    else:
        idx=i
        break;

result = ''
sum = 0

for i in range(idx,len(data)):
    result += data[i]
for i in range(0,idx):
    sum += int(data[i])

result += str(sum)

print(result)