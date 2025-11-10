def market(sell):
    count = 0 

    
    for i in range(1, len(sell)):
        if sell[i] < sell[i - 1]:
            count += 1

    print(f"매출이 전날보다 감소한 날은 {count}일입니다.")

sell = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
market(sell)