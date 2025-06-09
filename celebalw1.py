n = 5  # Number of rows

#lower triangular
for i in range(1, n + 1):
    print("* " * i)
#upper triangular
for i in range(n):
    print("  " * i + "* " * (n - i))
#pyramid 
for i in range(n):
    print("  " * (n - i - 1) + "* " * (2 * i + 1))

