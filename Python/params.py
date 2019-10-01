

def func(first, *args, **kwargs):
    print(first)
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 5, a=1, b=2)
