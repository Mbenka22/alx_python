for i in range (10):
    for j in range(i,10):
        print(f"{i:02d},{j:02d}" if i !=j else "", end=", "if j<9 else "\n")