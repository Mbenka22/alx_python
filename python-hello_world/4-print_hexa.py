for i in range(99):
    for j in range(i,99):
        print(f"{i:02d}", end=", " if i!=9 or j !=9 else "\n")
    