

print(ord('z'))

d = {i:-1 for i in range(97, 123)}
i=0
for s in input():
    d[ord(s)] = i if d[ord(s)] == -1 else d[ord(s)]
    i+=1
print(' '.join(map(str, d.values())))