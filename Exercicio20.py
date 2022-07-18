def fib_position(number):
    if number < 2:
        return number
    else:
        return fib_position(number-1) + fib_position(number-2)

def fibonacci(number):
    for n in range(number):
        print(fib_position(n), end=' ')