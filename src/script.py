from os import stat_result
import threading
import time


def measurement(func):
    def wrapper():
        start = time.time()
        func()
        print("実行時間: ", time.time() - start)

    return wrapper


@measurement
def loop():
    n = 10 ** 4
    for i in range(n):
        for j in range(n):
            pass


if __name__ == "__main__":
    t1 = threading.Thread(target=loop)
    t2 = threading.Thread(target=loop)
    t1.start()
    t2.start()
