data = []

for i in range(9):
    data.append(int(input()))

data.sort()
a = 0
b = 0

data_sum = sum(data)

for i in range(9):
    for j in range(i+1, 9):
        if data_sum - data[i] - data[j] == 100:
            a = data[i]
            b = data[j]

data.remove(a)
data.remove(b)

for i in data:
    print(i)
