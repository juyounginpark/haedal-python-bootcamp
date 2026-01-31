'''print(len("Python"))

print(sum([1,2,3]))

print(max(10,20,30))

print(type(3.14))'''


'''def greet(name):
    print(f"안녕하세요, {name}님!")

greet("철수")
greet("영희")

def add(a, b):
    return a + b

result = add(3,5)
print(result)

def print_star():
    print('************')

print_star()
print_star()'''


def print_star_n_times(n):
    for _ in range(n):
        print('************')

print_star_n_times(4)

def get_sum(a, b):
    result = a + b
    return result

sum_result = get_sum(10,20)
print('10과 20의 합 :', sum_result)

sum_result2 = get_sum(100,200)
print('100과 200의 합 :', sum_result2)
