from multiprocessing import Process
import os
from time import sleep


def func1(start, end):
    while start < end:
        print("Func1: %s" % start)
        start += 1
        sleep(1)


def func2(start, end):
    while start < end:
        print("Func2: %s" % start)
        start += 1
        sleep(1)


def func(start, end, timeout):
    while start < end:
        print(f"Process {os.getgid()}: {start}")
        start += 1
        sleep(timeout)


process1 = Process(target=func1, args = (3, 10))
process2 = Process(target=func2, args = (5, 20))
process3 = Process(target=func, args = (5, 20, 0.5))

if __name__ == '__main__':
    process1.start()
    process2.start()
    process3.start()
    print('END')
