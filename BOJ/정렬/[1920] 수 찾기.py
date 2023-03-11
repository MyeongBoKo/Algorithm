import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int,input().split())))
M = int(input())
numsM = list(map(int, input().split()))

def BSearch(nums, i, start, end):
    while start <= end:
        middle = (start + end)//2

        if nums[middle] == i:
            return 1
        else:
            if nums[middle] > i:
                end = middle - 1
            else:
                start = middle + 1

    return 0

for i in numsM:
    start = 0
    end = len(nums) - 1
    print(BSearch(nums, i, start, end))
    
