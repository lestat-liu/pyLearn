

import time
def make_time(func):
    def wrapper():
        t1 = time.time()
        rel = func()
        t2 = time.time()
        print("运行时间为： ", t2-t1)
        return rel
    return wrapper

@make_time
def a():
    time.sleep(2)


if __name__ == '__main__':
    a()

