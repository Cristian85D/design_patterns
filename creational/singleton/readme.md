# Singleton

# Definitions
- Classification: creational.
- Sometimes, you simply cannot have more than one instance of an object.
- Ensure a class has only one instance.
- This is handy, even necessary when you need to control access to a limited resource such as our hardware device, a 
set of buffer pools or connection pools for a web server or database access.
- Provides a global point of access to its one instance and is responsible for creating that instance.
- Singleton can also provide for lazy instantiation, which can be important if the object is costly to instantiate or 
may not always be used.

# Base class for all Singleton
- Keeps track of all singleton instances in a dictionary where the keys are class references and the values are 
instance references.
- Build a base class for all singletons.
- Inherit from the base class for each instance.

```python
import sqlite3


class Singleton:
    __instances = {}

    def __new__(cls):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__new__(cls)
        return cls.__instances[cls]


class Database1(Singleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('database1.sqlite3')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


class Database2(Singleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('database2.sqlite3')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


if __name__ == '__main__':
    db11 = Database1().connect()
    db12 = Database1().connect()
    print(db11, db12)

    db21 = Database2().connect()
    db22 = Database2().connect()
    print(db21, db22)
```

# Lazy instantiation
- Makes sure that the object gets created when it’s actually needed.
- Consider lazy instantiation as the way to work with reduced resources and  create them only when needed.

```python
class Singleton:
    def __init__(self):
        if '_instance' not in Singleton.__dict__:
            print(f'init method called')
        else:
            print(f'Instance already created: {self.get_instance()} ')

    @classmethod
    def get_instance(cls):
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()
        return Singleton._instance


if __name__ == '__main__':
    s1 = Singleton() # class initialized but _instance not created
    print(f'Object created: {Singleton.get_instance()}')  # object gets created here
    s2 = Singleton()  # instance already created
```

# Monostate
All the instances share the same state.

```python
class MonoState:

    __shared_states = {
        'CNF': 'Confirmed',
        'CAN': 'Cancelled',
        'REJ': 'Rejected'
    }

    def __new__(cls):
        if '_instance' not in MonoState.__dict__:
            MonoState._instance = super().__new__(cls)
            MonoState._instance.__dict__ = MonoState.__shared_states
        return MonoState._instance


class Singleton(MonoState):
    pass


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(f's1: {s1}. s1.__dict__: {s1.__dict__}')
    print(f's2: {s2}. s2.__dict__: {s2.__dict__}')
```
