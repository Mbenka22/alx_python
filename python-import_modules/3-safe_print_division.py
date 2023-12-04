def safe_print_division(a, b):
    a=12
    b=0
    b=2
    try:
        result = a / b
    except :
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))




a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))