a = int(input("Enter the dimension: "))

for i in range(1, a + 1):
    for j in range(i, a + i):
        if j > a:
            j = j - a
        print(j, end=" ")
    print("/n")
