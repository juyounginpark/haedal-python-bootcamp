def analyze_tuple(tup):
    freq = {}  

  
    for item in tup:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    print("각 원소의 등장 횟수:")
    for key, value in freq.items():
        print(f"{key}: {value}번")

  
    max_item = max(freq, key=freq.get)
    print(f"\n가장 많이 나타나는 요소: {max_item} (총 {freq[max_item]}번)")

tup = (1, 3, 2, 3, 1, 3, 2, 4, 3)
analyze_tuple(tup)