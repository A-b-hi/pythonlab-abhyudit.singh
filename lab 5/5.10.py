def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

def square(x):
    return x * x

def square_fibonacci(n):
    fib_numbers = fibonacci(n)
    return list(map(square, fib_numbers))

N = 10
result = square_fibonacci(N)
print(result)