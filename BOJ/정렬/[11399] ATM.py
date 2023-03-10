n = int(input())
nums = list(map(int,input().split()))

nums.sort()
answer = 0

for i in range(1, n+1):
    answer += sum(nums[0:i])
print(answer)

