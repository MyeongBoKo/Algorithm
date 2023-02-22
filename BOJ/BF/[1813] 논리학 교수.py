N = int(input())
num_arr = list(map(int,input().split()))

num_index = [0]*100
answer_arr = []

for i in range(N):
    num_index[num_arr[i]] += 1

for a in range(len(num_index)):
    if num_index[a]==a:
        answer_arr.append(a)

if len(answer_arr) == 0:
    print(-1)
else:
    print(answer_arr[-1])
