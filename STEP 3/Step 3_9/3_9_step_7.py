class Integer:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z


pt = Point3D(1, 2, 3)