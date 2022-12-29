a, b = map(int,input().split())
ans =[0]
sum = 0
for i in range(1, b+1):
    for j in range(i):
        ans.append(i)
        
for i in range(a, b+1):
    sum += ans[i]
print(sum)
