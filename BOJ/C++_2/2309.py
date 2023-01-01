array = [int(input()) for _ in range(9)]
array.sort()

sum_ = sum(array)

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if sum_ - array[i] - array[j] == 100:
            for k in range(len(array)):
                if k == i and k == j:
                    pass
                else:
                    print(array[k])


