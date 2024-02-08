n = int(input())

a = [0, 1, 2, 3]
for i in range(3, n):
    a.append(a[i-1]+a[i])

print(a[n]%10007)