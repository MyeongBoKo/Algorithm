def check(result):
    num_of_zero = result.count(0)
    if num_of_zero == 0:
        print("E")
    elif num_of_zero == 1:
        print("A")
    elif num_of_zero == 2:
        print("B")
    elif num_of_zero == 3:
        print("C")
    else:
        print("D")

for i in range(3):
    result = list(map(int, input().split()))
    check(result)
            
