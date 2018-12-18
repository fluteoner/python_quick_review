import random

def gensquares(N):
    for count in range(N):
        yield count**2


def rand_num(low, high, n):
    for x in range(1, n):
        yield random.randint(low, high)


if __name__ == '__main__':

    # Generator
    for x in gensquares(10):
        print(x)
    for num in rand_num(1, 10, 12):
        print(num)

    # Iterator
    s = 'hello'
    s = iter(s)
    print(next(s))

