# Define variables a and b
if __name__=="_main_":
    a=1
    b=2

    #import the add function
    from add_0 import add

    #perform the addition and print the result
    result=add(a,b)
    print("{}+{}={}".format(a,b,result))
