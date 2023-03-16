class Singleton1:
    val = None

    @staticmethod
    def instance():
        """
        The class definition provides a static instance method to use to
        access that one instance. Now this method does a little reflection
        and looks to see if the variable, _instance, is already defined in the
        class dictionary. If not, it instantiates a new one and saves that
        reference in the _instance variable which also causes it to be added
        to the class dictionary for the next time around.
        """
        if '_instance' not in Singleton1.__dict__:
            Singleton1._instance = Singleton1()
        return Singleton1._instance


def main_singleton1():
    """
        I call the instance method twice for two different variables and
        then test their equality.
        """
    s1 = Singleton1.instance()
    s2 = Singleton1.instance()

    s1.val = 42

    if id(s1) == id(s2):
        print('Represent the same object in memory')
        print(id(s1), id(s2))
        print(f's1 val: {s1.val} . s2 val: {s2.val}')


class Singleton2:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

def main_singleton2():
    s21 = Singleton2()
    s22 = Singleton2()

    if id(s21) == id(s22):
        print('Represent the same object in memory')
        print(f'{id(s21)}, {id(s22)}')


class Singleton3:
    def __new__(cls):
        # if not hasattr(cls, '_instance'):
        #     cls._instance = super().__new__(cls)
        # return cls._instance

        if '_instance' not in cls.__dict__:
            cls._instance = super().__new__(cls)
        return cls._instance

def main_singleton3():
    s31 = Singleton3()
    s32 = Singleton3()

    if id(s31) == id(s32):
        print('Represent the same object in memory')
        print(f'{id(s31)}, {id(s32)}')


if __name__ == '__main__':
    # main_singleton1()
    # main_singleton2()
    main_singleton3()
