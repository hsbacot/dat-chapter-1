# start at 2 because loops starts after first two fib numbers
even_sum = 2
fib = [1, 2]
fib_length = len(fib)

while fib[fib_length - 1] < 4000000:
    next_num = fib[fib_length - 1] + fib[fib_length - 2]
    if next_num % 2 == 0:
        even_sum = even_sum + next_num
    fib.append(next_num)
    fib_length = len(fib)


print(even_sum)
