def safe_print_division(a, b):
    a=12
    b=2
    #!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

print("Result:", result)

result = safe_print_division(12, 2)
print("Result:", result)
