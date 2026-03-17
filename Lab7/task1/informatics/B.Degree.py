# Function to calculate a^n
def power(a, n):
    result = 1.0
    for _ in range(n):
        result *= a
    return result
a, n = input().split()
a = float(a)
n = int(n)

print(power(a, n))