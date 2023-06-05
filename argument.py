# args is tuple 
def func(a, b, *args):
    print(a, b)
    for x in args: 
        print(x)

# kargs is dict    
def func2(**kargs):
    for (key, value) in kargs.items():
        print(key, value)
func(123, 456, 454)
func2(c = 4, a = 2)