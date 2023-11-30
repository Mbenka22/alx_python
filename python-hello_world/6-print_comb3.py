for i in range(0, 10):
    for j in range(i + 0, 10):
        print(f"{i}{j}", end=", " if i != 9 or j != 8 else "\n")      