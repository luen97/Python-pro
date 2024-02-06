from time import sleep
def fibonacci_gen(max_val):
    a, b = 0, 1
    while a < max_val:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    fibonacci = fibonacci_gen(10)
    for element in fibonacci:
        print(element)
        sleep(1)