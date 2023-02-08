n = int(input())
ans = 0

for i in range(1, n+1):
    if i < 100:
        ans += 1
    
    else:
        nums = list(map(int, str(i)))
        if nums[2] - nums[1] == nums[1] - nums[0]:
            ans += 1

print(ans)
