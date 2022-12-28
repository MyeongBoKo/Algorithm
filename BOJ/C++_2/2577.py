A=int(input())
B=int(input())
C=int(input())

ans_list = []
result = str(A*B*C)

for i in range(len(result)):
    ans_list.append(int(result[i]))

for i in range(10):
    print(ans_list.count(i))
