N=int(input())
for i in range(1,N+1):
    for _ in range(1,(N-i)+1):
        print(" ",end="")
    for _ in range(1,i+1):
        print("*",end="")
    print()

