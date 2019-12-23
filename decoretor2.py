from time import time
def timer(any_function):
    def count_time():
        start = time()
        any_function()
        stop = time()
        print(stop - start,'seconds')
        return
    return count_time

@timer
def hello():
    print("Hello World")
    return
@timer
def another_fun():
    for i in range(1,11):
        print(i)
    return

hello()
another_fun()
