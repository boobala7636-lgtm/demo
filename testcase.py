x = [10,20,30]

for i in range(len(x)):
    x[i] = x[x[i]//10 -1]

print(x)
