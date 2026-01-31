# 문제 2: 단어 수 세기

f = open("python-bootcamp\input2.txt", "r")
text = f.read()  
f.close()

words = text.split()
print("단어의 개수:", len(words))



































































































# f = open("count_word.txt", "r")
# text = f.read()              # 전체 내용 읽기
# f.close()

# words = text.split()         # 공백 기준으로 단어 분리
# print("단어의 개수:", len(words))