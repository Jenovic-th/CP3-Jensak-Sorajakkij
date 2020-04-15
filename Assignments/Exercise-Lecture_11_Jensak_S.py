Number = int(input("Please input Size Pyramid"))
for x in range(Number):
    print(" " * (Number - x - 1) + "*" * (x * 2 + 1))