try:
    a = int(input("숫자를 입력하세요 : "))
    print(10/a)
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다!")
print("프로그램 끝!")