numbers = []

for i in range(9):
    n = int(input())
    numbers.append(n)

max_num = max(numbers)
max_index = numbers.index(max_num) + 1

print(max_num)
print(max_index)
