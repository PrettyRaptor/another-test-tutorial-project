from multiprocessing import Process, Value, Array, Lock, Queue
import os
import time
import datetime as dt

def process_load():
    for i in range(100):
        i ** 2
        # print(i)
        time.sleep(0.01)

def increase(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1
    print(f'number now is: {number.value}')

def increase_without_lock(number):
    for _ in range(100):
        time.sleep(0.01)
        number.value += 1
    print(f'number now is: {number.value}')

def increase_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

def square(numbers, queue):
    for i in numbers:
        queue.put(i * i)

def negative(numbers, queue):
    for i in numbers:
        queue.put(-1 * i)

if __name__ == "__main__":

    # shared_value = Value('i', 0)
    # print(f'number at start: {shared_value.value}')

    # shared_array = Array('d', [0.0, 100.0, 200.0, 0.001])
    # print(f'array at start: {shared_array[:]}')

    lock = Lock()

    # p1 = Process(target=increase, args=(shared_value, lock))
    # p2 = Process(target=increase, args=(shared_value, lock))
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    num_processes = os.cpu_count()
    processes = []
    # for _ in range(num_processes):
    #     p = Process(target=increase_array, args=(shared_array, lock))
    #     processes.append(p)
    #     p.start()

    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=negative, args=(numbers, q))

    processes.append(p1)
    processes.append(p2)

    for p in processes:
        p.start()

    for p in processes:
        p.join()


    # print(f'number at finish: {shared_value.value}')
    # print(f'array at finish: {shared_array[:]}')

    while not q.empty():
        print(q.get())

    print('end main')



