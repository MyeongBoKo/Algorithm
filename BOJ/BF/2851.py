num_arr = []
for _ in range(10):
    num_arr.append(int(input()))
sum = 0
for i in num_arr:
    sum += i
    if sum >= 100:
        if sum-100 > 100-(sum-i):
            sum -= i
        break
print(sum)
