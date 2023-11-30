def add(a, b):
    # Using bitwise operations to simulate addition
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
print (add(1,2))