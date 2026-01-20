rows = 10
ascii_value = 65  # ASCII value of 'A'

for i in range(1, rows + 1):
    for j in range(i):
        print(chr(ascii_value + j), end="")
    print()


