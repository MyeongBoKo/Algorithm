n = int(input())
num_list = list(map(int, input().split()))
count = 0

for x in num_list:
    cnt = 0
    if x==1:
        continue
    for i in range(2, x):
        if x%i == 0:
            cnt += 1
    if cnt == 0:
        count += 1

print(count)
