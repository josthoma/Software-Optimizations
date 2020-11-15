'''

Basic Example without Thread
'''


import time

def myfunc(i):
    print (f"sleeping 5 sec from thread {i}")
    time.sleep(5)
    print (f"finished sleeping from thread {i}")

for i in range(3):
    myfunc(i)