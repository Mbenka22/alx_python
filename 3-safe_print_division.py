def safe_print_division(a, b):
    a=12
    b=2
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))

# Test cases
result = safe_print_division(10, 2)
print("Result:", result)

result = safe_print_division(5, 0)
print("Result:", result)
