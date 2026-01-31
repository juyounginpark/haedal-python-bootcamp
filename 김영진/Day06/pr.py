'''nums = range(1,11)
list_nums = list(nums)

nums_sq = map(lambda x: x**2, nums)
print(list(nums_sq))'''



nums = range(0,101)
list_nums = list(nums)

nums_sq = []
for num in nums:
    if num % 12 == 0:
        nums_sq.append(num)
print(nums_sq)
        



nums_even = filter(lambda x: x%12 == 0, nums)
print(list(nums_even))

nums_sq = [x for x in nums if x%12 == 0]
print(nums_sq)