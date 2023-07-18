#------------------------------------#
# Starting code
#------------------------------------#

# import time
# current_time = time.time()
# print(current_time)

# def speed_calc_decorator():
#     pass

# def fast_function():
#     for i in range(10000000):
#         i * i
        
# def slow_function():
#     for i in range(100000000):
#         i * i
        
#------------------------------------#
# Ending code
#------------------------------------#

import time
current_time = time.time()
# print(current_time)

def speed_calc_decorator(speed_function):
    def wrapper_function():
        start_time = current_time
        speed_function()
        end_time = time.time()
        difference = end_time - start_time
        print(f"{speed_function.__name__} run speed: {difference}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator       
def slow_function():
    for i in range(100000000):
        i * i
        
fast_function()
slow_function()