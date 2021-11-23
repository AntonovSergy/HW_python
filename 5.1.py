def gen_nums(maximum):
    n = 1
    while n <= maximum:
        yield n
        n += 2

odd_to_15 = gen_nums(20)