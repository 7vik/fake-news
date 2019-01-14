i = 53
f = open("./"+str(i).zfill(3)+"fake.txt", "r+")
print(f.readline())
print(''.join(f.read().split('\n')))