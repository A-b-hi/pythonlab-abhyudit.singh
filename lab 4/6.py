for i in range(1, 6):
    print(' ' * (5-i) + ' '.join(str(j) for j in range(i, 0, -1)))