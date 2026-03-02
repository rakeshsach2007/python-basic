import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@measure_time
def sample_function():
    for i in range(1000000):
        pass

@measure_time
def testfunc():
    for i in range(5):
        for i in range(1000000):
            pass
        
    print("testFunc - done")
             
sample_function()

testfunc()

#testfunc()

print("function executed")