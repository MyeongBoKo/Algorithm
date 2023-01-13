import sys
input = sys.stdin.readline

n = int(input())            
broken_n = int(input())
broken_arr = list(map(int, input().split()))

min_num = abs(100-n)

for channel in range(1000000):
    num = str(channel)
    
    for j in range(len(num)):
        if int(num[j]) in broken_arr:
            break

        elif j == len(num)-1:
            min_num = min(min_num, len(num) + abs(channel - n))
print(min_num)
