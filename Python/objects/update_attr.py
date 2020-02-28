

class temp:

    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
        self.e = e
        self.f = f


if __name__ == "__main__":
    new_temp = temp(1, 2, 3, 4, 5, 6)

    new_values = dict(a=2, c=4, e=6)

    for k, v in new_values.items():
        setattr(new_temp, k, v)

    print(new_temp.__dict__)

    setattr(new_temp, 'a', 0)

    print(new_temp.__dict__)

    map(lambda x: setattr(new_temp, *x), new_values.items())

    print(new_temp.__dict__)
