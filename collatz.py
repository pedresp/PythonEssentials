c0 = int(input("Insert a number:\n"))

count = 0
while c0 != 1:
    if not c0 % 2:
        c0 = int(c0 / 2)
    else:
        c0 = 3 * c0 + 1
    print(c0)
    count += 1

print("steps =", count)