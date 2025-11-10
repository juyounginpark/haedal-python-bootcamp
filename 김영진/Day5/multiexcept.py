try:
    nums = [1,2,3]
    print(5/0)
except IndexError:
    print("리스트 범위를 벗어났어요!")
except Exception as e:
    print("다른 오류가 발생했어요:", e)