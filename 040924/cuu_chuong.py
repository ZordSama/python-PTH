for i in range(1, 11):
    for j in range(1, 10):
        print(f"{j} x {i} = {i * j}", end="\t")
    print()
print("\n")
print(" ", end="\t")
for i in range(1, 10):
    print("\033[91m" + str(i) + "\033[0m", end="\t")
print("\n")
for i in range(1, 10):
    print("\033[91m" + str(i) + "\033[0m", end="\t")
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")