# def add_num(a, b):
#    return a + b
#
#
# def print_info(func):
#    def wrapper(*args, **keyargs):
#        print("start")
#        result = func(*args, **keyargs)
#        print("end")
#        return result
#
#    return wrapper
#
#
# f = print_info(add_num)
# f(10, 20)
#


def print_info(func):
    def wrapper(*args, **keyargs):
        print("start")
        result = func(*args, **keyargs)
        print("end")
        return result

    return wrapper


@print_info
def add_num(a, b):
    return a + b


print(add_num(10, 20))
