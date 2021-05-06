from  functools import wraps
import time
def print_function(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        t1=time.time()
        if all([type(arg)==int for arg in args]):
            t2=time.time()
            t3=t2-t1
            print(f"you take a {t3} time")
            return function(*args,**kwargs)
        print("invalid argument")
        t2=time.time()



    return  wrapper


@print_function
def add_all(*args):
    total=0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4,5,6,7))