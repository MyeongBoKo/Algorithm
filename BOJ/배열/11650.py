result = []
for _ in range(int(input())):
    result.append(list(map(int,input().split())))

result.sort(key=lambda x:(x[0], x[1]))

for i in result:
    print(str(i[0])+' '+str(i[1]))

