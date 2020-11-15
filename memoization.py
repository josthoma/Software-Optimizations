import time

cache = {}
def measure(function, parameter):
    begin = time.perf_counter()
    print(begin)
    result = function(parameter)
    end = time.perf_counter()
    duration = end - begin

    return result, duration

def memoization(num):
    print('Running Function...')
    time.sleep(1)
    mul = num**99999
    cache[num] = mul
    return  mul


mul, dur = measure(memoization,244554461111)
print(f"time :{dur:2.8f} sec")
mul, dur = measure(memoization, 244554461111)
print(f"time :{dur:2.8f} sec")
mul, dur = measure(memoization,244554461111)
print(f"time :{dur:2.8f} sec")
mul, dur = measure(memoization, 244554461111)
print(f"time :{dur:2.8f} sec")
mul, dur = measure(memoization,244554461111)
print(f"time :{dur:2.8f} sec")
mul, dur = measure(memoization, 244554461111)
print(f"time :{dur:2.8f} sec")
