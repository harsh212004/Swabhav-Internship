# Increasing Triangle
print("\nIncreasing Triangle\n")
n = 5
for i in range(1,n+1):
    print("* " * i)
print()

# Decreasing Triangle
print("Decreasing Triangle\n")
n = 5
for i in range(n,0,-1):
    print("* " * i)
print()

# Hill Pattern
print("Hill Pattern\n")
n = 9
for i in range(n):
    print(" " * (n-i-1) + "* " * (i+1))
print()

# Reverse Hill Pattern

print("Reverse Hill Pattern\n")
n=9
for i in range(n,0,-1):
    print(" " * (n-i) + "* " * i)
print()