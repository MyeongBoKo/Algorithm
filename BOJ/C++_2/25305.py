import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse = True)

ans = []
for i in range(k):
    ans.append(arr[i])
    
print(ans[-1])
