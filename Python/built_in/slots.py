# The slots biult-in function is used to define the attributes a class can receive.
# This list is unmutable, so no attr can be removes or added

class WithOutSlots:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class WithSlots:

    __slots__ = ('x', 'y', 'z')

    def __str__(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + str(self.z)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def instance_fn(cls):

    def instance():
        x = cls(1, 2, 3)

    return instance


if __name__ == "__main__":
    import timeit
    ws = WithSlots(x=dict(uno=1, dos=2), y='string', z=23)
    ws.x = 'cambiamos esto'
    print(ws)
    print(timeit.timeit("instance_fn(WithOutSlots)", setup="from __main__ import instance_fn, WithOutSlots"))
    print(timeit.timeit("instance_fn(WithSlots)", setup="from __main__ import instance_fn, WithSlots"))
