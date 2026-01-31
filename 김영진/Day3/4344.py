C = int(input())  

for _ in range(C):
    data = list(map(int, input().split()))
    N = data[0]  
    scores = data[1:]  
    
    avg = sum(scores) / N  
    
    count = 0
    for s in scores:
        if s > avg:
            count += 1
    
    rate = (count / N) * 100
    
    print(f"{rate:.3f}%")
