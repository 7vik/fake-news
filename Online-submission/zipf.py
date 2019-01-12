#Pravega Hackathon Submission

i = 200000              #Number of words in English
sum = 0
for r in range(1,i):
    sum += 1/r

print(sum)

sum /= 2                #We wanna cover half the words
t = 1

while sum>0:
    sum -= 1/t
    t += 1

print(t)
