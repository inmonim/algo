
import random

with open('input.txt', 'w') as f:
    for y in range(100):
            x = ' '.join(map(str, [random.randint(0, 1) if y!=i else 0 for i in range(100)]))+'\n'
            f.write(x)
