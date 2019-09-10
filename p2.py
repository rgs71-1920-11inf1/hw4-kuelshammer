a = 0
b = 3

while a < b:
    if a % 2 == 0:
        a = a + 1
        b = b - 1
    else:
        a = 2 * a + 1
        b = b + 2
    print(a)
