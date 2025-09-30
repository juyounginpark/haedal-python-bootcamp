N = int(input())
numbers = list(map(int, input().split()))
prime_count = 0

for num in numbers:
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        prime_count += 1
print(prime_count)