# timing function
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print (f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper
    
@timer
def examplefunc(n):
    time.sleep(n)
# examplefunc(1)


# debugging function

def debug(func):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(arg) for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    
    return wrapper

@debug
def hello():
    print("hello")
    
@debug
def greet(name, greeting="Hello"):
    print(f"{greeting},{name}")
    
# hello()
# greet("Utkrishta",greeting="Namaste!")


# cache return values

def cache(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def long_run_func(a,b):
    time.sleep(4)
    return a + b
    
print(long_run_func(5,6))
print(long_run_func(5,6))
print(long_run_func(5,4))



    