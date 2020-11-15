from functools import lru_cache
import time
####################################################################
# Generating the Fibonacci Sequence: fb(n) = fb(n-1) + fb(n-2)
# 0, 1,
# 0, 1, 1,
# 0, 1, 1, 2,
# 0, 1, 1, 2, 3,
# 0, 1, 1, 2, 3, 5,
# 0, 1, 1, 2, 3, 5, 8,
# 0, 1, 1, 2, 3, 5, 8, 13,
# 0, 1, 1, 2, 3, 5, 8, 13, 21,
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


def measure(function, parameter):
    begin = time.clock()
    result = function(parameter)
    end = time.clock()
    duration = end - begin

    return result, duration


# Caching: Example 1
def naiveFib(n):
    if n < 2:
        return n
    return naiveFib(n-1) + naiveFib(n-2)


@lru_cache(maxsize=None)
def lruFib(n):
    if n < 2:
        return n
    return lruFib(n-1) + lruFib(n-2)

f1, duration1 = measure(naiveFib, 5)
f2, duration2 = measure(lruFib, 5)

print(f'Naive Fibonacci = {f1}   Duration = {duration1:2.9f} sec')
print(f'  LRU Fibonacci = {f2}   Duration = {duration2:2.9f} sec')

# Caching: Example 2
@lru_cache(maxsize=None)
def func2(n):
    print(f"Input = {n}")
    time.sleep(2)
    return n

for i in [0, 1, 2, 0, 1, 2, 0, 1, 2]:
    r = func2(i)
    print(f"   r = {r}")