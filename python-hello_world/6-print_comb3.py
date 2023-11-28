for i in range (10):
    for j in range(i,10):
        print(f"{i:02d}",end=", "if i!=9 or j!=9 else "\n".format(i))
        