n, m = map(int, input().split())
nums = list(map(int,input().split()))

total = nums[0]
left, right = 0, 0
cnt = 0

while True:
    if total < m:
        right += 1
        if right < n:
            total += nums[right]
        else:
            break
    elif total == m:
        cnt += 1
        total -= nums[left]
        left += 1
    else:
        total -= nums[left]
        left += 1
print(cnt)
