num_arr = [int(input()) for _ in range(9)]
sum_num = sum(num_arr)

for i in range(len(num_arr)):
    for j in range(i+1, len(num_arr)):
        if sum_num - num_arr[i] - num_arr[j] == 100:
            for k in range(len(num_arr)):
                if k==i or k==j:
                    pass
                else:
                    print(num_arr[k])
            
