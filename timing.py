import time
"""
Take a function to calculate the time that it took to run this function.
Parameter
func:
	a function
Return
run time of the function.
"""
def calculate_time(func):
    """
    take parameters put in function and run function to get the run time of this function.
    Parameter
    **kwargs
    	These parameters will be passed to the matplotlib ploting function.
    """
    def timer(*args, **kwargs):
        start_time = time.time()
        x = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f'Total time',run_time)
        return x
    return timer
@calculate_time
def func():
	time.sleep(2)
func()
