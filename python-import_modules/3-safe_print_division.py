def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))

# Test cases
result = safe_print_division(12, 2)
print("Result:", result)

result = safe_print_division(12, 0)
print("Result:", result)
