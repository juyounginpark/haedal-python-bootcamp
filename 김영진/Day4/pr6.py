def set_operations(a, b):
    
    union = []
    for x in a:
        if x not in union:
            union.append(x)
    for y in b:
        if y not in union:
            union.append(y)


    intersection = []
    for x in a:
        if x in b and x not in intersection:
            intersection.append(x)

  
    difference_a_b = []
    for x in a:
        if x not in b:
            difference_a_b.append(x)

    difference_b_a = []
    for x in b:
        if x not in a:
            difference_b_a.append(x)

   
    print(f"합집합: {union}")
    print(f"교집합: {intersection}")
    print(f"차집합 a-b: {difference_a_b}")
    print(f"차집합 b-a: {difference_b_a}")

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
set_operations(a, b)