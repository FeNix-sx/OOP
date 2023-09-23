class Example:
    def __init__(self):
        self.__model = None

    def __new__(cls, *args, **kwargs):
        pass

    @staticmethod
    def out(string):
        return int(string)

    @classmethod
    def check_name(cls, name: str):
        return name

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    def __add__(self):
        """для операции сложения;"""
    def __sub__(self):
        """для операции вычитания;"""
        pass
    def __mul__(self):
        """для операции умножения;"""
        pass
    def __truediv__(self):
        """для операции деления."""
        pass

