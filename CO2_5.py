n = int(input("Enter the number of steps: "))

for i in range(1, n + 1):
    print(" ".join(str(i * j) for j in range(1, i + 1)))
    
