# start at 2 because loops starts after first two fib numbers
evenSum = 2
fib = [1, 2]
fibLength = len(fib)

while fib[fibLength - 1] < 4000000:
    nextNum = fib[fibLength - 1] + fib[fibLength - 2]
    if nextNum % 2 == 0:
        evenSum = evenSum + nextNum
    fib.append(nextNum)
    fibLength = len(fib)


print(evenSum)
