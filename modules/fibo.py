# Fibonacci numbers module

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# Executing modules as scripts
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    # python fibo.py 10000
