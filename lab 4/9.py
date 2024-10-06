start = 1
for i in range(1, 5):
    row = []
    for j in range(i):
        row.append(str(start))
        start += 1
    print(" ".join(row[::-1]))