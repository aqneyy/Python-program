import math
for i in range(1000,10000):
    sqrt = int(math.sqrt(i))
    if sqrt * sqrt == i:
        if all (int(digit) % 2 == 0 for digit in str(i)):
            print(i)