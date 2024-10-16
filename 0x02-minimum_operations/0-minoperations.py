
def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    current = n

    # We will find the factors of n
    for i in range(2, n + 1):
        while current % i == 0:  # while i is a factor of current
            operations += i  # Copy + Paste operations to reach i
            current //= i  # reduce current by factor i
    return operations

# Example usage
if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
