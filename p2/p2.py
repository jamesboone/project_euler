def fib(new, old):
    if not old:
        fib_num = new + new
    else:
        fib_num = new + old

    return fib_num


def sum_fib():
    sum_of_even_fibs = 0
    fib_num = 0
    start = 1
    for i in xrange(1, 1000000):
        old = fib_num
        fib_num = fib(start, fib_num)
        if fib_num > 4000000:
            print sum_of_even_fibs
            return
        elif fib_num % 2 == 0:
            sum_of_even_fibs = sum_of_even_fibs + fib_num

        if fib_num == 2:
            continue
        else:
            start = old
