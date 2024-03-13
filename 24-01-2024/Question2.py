def count_digits(N):
    count = 0
    while N != 0:
        N //= 10
        count += 1
    return count

# Input
N = int(input().strip())

# Count digits
result = count_digits(N)

# Output
print(result)
