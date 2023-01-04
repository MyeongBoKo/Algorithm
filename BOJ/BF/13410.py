N, k = map(int, input().split())

num_arr = []
for i in range(1,k+1):
    res = N*i
    num_arr.append(res)

ans_arr = []
for j in range(len(num_arr)):
    num_str = str(num_arr[j])
    num_str = num_str[::-1]
    ans_arr.append(int(num_str))

print(max(ans_arr))
