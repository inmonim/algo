a, b, c= 123423, 5, 9933

x = (((a%c) ** 2) * ((a%c) ** 2) * (a%c)) % c

y = ((a**5) % c)

print(x)
print(y)