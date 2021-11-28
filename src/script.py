import multiprocessing
import time


def measurement(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print("実行時間: ", time.time() - start)

    return wrapper


def loop(n):
    for i in range(n):
        for j in range(n):
            pass


if __name__ == "__main__":
    proccess_num = 2
    with multiprocessing.Pool(proccess_num) as p:
        p.map(loop, [4, 4])
