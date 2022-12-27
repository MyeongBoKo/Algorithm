M = int(input())
N = int(input())

num_list = []
for x in range(M, N+1):
    count = 0
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                count += 1
                break
        if count == 0:
            num_list.append(x)

if len(num_list)!=0:
    print(sum(num_list))
    print(num_list[0])
else:
    print(-1)

