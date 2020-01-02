
class Factory(object):
    
    @classmethod
    def get_object(cls, name):
        from classa import ClassA
        cls = getattr(classa, name)
        return cls()

    @classmethod
    def reflection(cls, name):
        obj = globals().get(name)
        ins = obj()
        print(ins.suma(2, 4))


a = Factory.get_object('ClassA')

print(a.suma(2, 4))
