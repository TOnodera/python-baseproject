import os


def fils_is_empty(path):
    return os.stat(path).st_size == 0
