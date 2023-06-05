def hello_decorator(func):
    def wrapper():
        print(f'begin {func.__name__}')
        func()
        print("end")
    return wrapper
        
def display():
    print("inside function")    
    
@hello_decorator
def display2():
    print("inside function")
    
print(display.__name__)

# temp = hello_decorator(display)
# temp()
# display2()