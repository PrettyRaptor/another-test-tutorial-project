from threading import Thread, Lock, current_thread
from queue import Queue


import os
import time
import datetime as dt


DB_value = 0
def increase(lock):
    global DB_value

    # lock.acquire()
    # local_copy = DB_value
    # local_copy += 1
    # time.sleep(0.1)
    # DB_value = local_copy
    # lock.release()

    with lock:
        local_copy = DB_value
        local_copy += 1
        time.sleep(0.1)
        DB_value = local_copy

def worker(q, lock):
    while True:
        value = q.get()
        #... processing
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

def worker_without_lock(q):
    while True:
        value = q.get()
        #... processing
        print(f'in {current_thread().name} got {value}')
        q.task_done()



if __name__ == "__main__":

    # lock = Lock()
    # print(f'start value: {DB_value}')
    #
    # thread1 = Thread(target=increase, args=(lock,))
    # thread2 = Thread(target=increase, args=(lock,))
    #
    # thread1.start()
    # thread2.start()
    #
    # thread1.join()
    # thread2.join()
    #
    # print(f'finish value: {DB_value}')

    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon=True
        thread.start()

    for i in range (1, 27):
        q.put(i)

    q.join()

    print('end main')