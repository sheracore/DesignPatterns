import time

def time_measurement(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {int(end - start)*1000}ms")
    return wrapper


@time_measurement
def test():
    print(f"Testing")
    time.sleep(1)

test()