n = int(input())
n_list = list(map(int, input().split()))

sum = 0
sum_list = 0
for i in n_list:
    if i == 1:
        sum += 1
        sum_list += sum
    else:
        sum = 0
print(sum_list)
    
