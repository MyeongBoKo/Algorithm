N, M = map(int, input().split())
num_ = list(map(int, input().split()))
result = 0

for i in range(len(num_)):
    for j in range(i+1, len(num_)):
        for k in range(j+1, len(num_)):
            if num_[i] + num_[j] + num_[k] > M:
                pass
            else:
                result = max(result, num_[i] + num_[j] + num_[k])
print(result)
