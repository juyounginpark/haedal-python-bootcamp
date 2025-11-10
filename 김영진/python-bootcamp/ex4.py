# 문제 4: 숫자 파일의 합 구하기
f = open("python-bootcamp/numbers.txt", "r")
total = 0
for line in f:
    num = int(line.strip())
    total += num
    f.close()
print("합계:", total)

































































































# f = open("numbers.txt", "r")

# total = 0
# for line in f:
#     num = int(line.strip())   # 줄 끝의 개행문자 제거 후 정수로 변환
#     total += num

# f.close()

# print("합계:", total)