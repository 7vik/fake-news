i = 300000
sum = 0
for r in range(1,i):
    sum += 1/r

print(sum)
sum /= 2
t = 1

while sum>0:
    sum -= 1/t
    t += 1

print(t)
