n = int(input())
result = list(map(int, input().split()))
ans = []

for i in range(n):
    ans.append(result[i]/max(result)*100)

print(sum(ans)/n)
