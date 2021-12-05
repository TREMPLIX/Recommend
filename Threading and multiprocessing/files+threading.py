import datetime
from time import sleep
#from multiprocessing import Process
from threading import Thread
data = 'Текущее время {} \n'.format(datetime.datetime.now().time())


def func(count):
    f = open('temp1.txt', 'w')
    f.close()
    for i in range(count):
        f = open('temp1.txt', 'a')
        data = 'Текущее время {} \n'.format(datetime.datetime.now().time())
        f.write(data)
        sleep(1)
        f.close()


def func_2(count):
    f = open('temp2.txt', 'w')
    f.close()
    for i in range(count):
        f = open('temp2.txt', 'a')
        data = 'Текущее время {} \n'.format(datetime.datetime.now().time())
        f.write(data)
        sleep(2)
        f.close()


if __name__ == '__main__':
    #process_1 = Process(target=func, args=(10, ))
    #process_2 = Process(target=func_2, args=(10, ))
    thread_1 = Thread(target=func, args=(10, ))
    thread_2 = Thread(target=func_2, args=(10, ))
    #process_1.start()
    #process_2.start()
    thread_1.start()
    thread_2.start()
    print('END', 'Текущее время {} \n'.format(datetime.datetime.now().time()))

