def power(base, index):
    return base ** index

bases = [2, 3, 4, 5]

result = list(map(power, bases, range(len(bases))))

print(result)