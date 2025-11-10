# 문제 3: 파일 복사하기

# 1. 원본 파일(source.txt)을 읽기 모드로 연다.
src = open("python-bootcamp\input3.txt", "r", encoding = 'utf-8')

# 2. 새 파일(copy.txt)을 쓰기 모드로 연다.
copy = open("python-bootcamp\copy.txt", "w", encoding = "utf-8")

# 3. 원본 파일에서 한 줄씩 읽어서 복사
for line in src:
    copy.write(line)

src.close()
copy.close()

print("파일 복사가 완료되었습니다.")





















































































# # 1. 원본 파일(source.txt)을 읽기 모드로 연다.
# src = open("input3.txt", "r", encoding="utf-8")

# # 2. 새 파일(copy.txt)을 쓰기 모드로 연다.
# dst = open("copy.txt", "w", encoding="utf-8")

# # 3. 원본 파일에서 한 줄씩 읽어서 복사
# for line in src:
#     dst.write(line)

# # 4. 파일 닫기
# src.close()
# dst.close()

# print("파일 복사가 완료되었습니다.")