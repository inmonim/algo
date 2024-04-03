import array, sys, random

arr = array.array('i', [])
list = []

for i in range(100000):
    x = random.randint(0, 9)
    list.append(x)
    arr.append(x)

print(sys.getsizeof(list))
print(sys.getsizeof(arr))