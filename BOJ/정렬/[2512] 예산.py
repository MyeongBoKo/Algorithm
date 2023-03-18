import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
target = int(input())

start, end = 0, max(nums)

while start <= end:
    mid = (start+end)//2

    num = 0
    for i in nums:
        if i >= mid:
            num += mid
        else:
            num += i

    if num <= target:
        start = mid + 1
    else:
        end = mid - 1

print(end)
    
    
