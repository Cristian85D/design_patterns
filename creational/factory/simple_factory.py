import sys

from abc import ABC, abstractmethod
from inspect import getmembers, isclass, isabstract

"""
We eliminated the open‑closed violation.
Now it's simple to add new cars.

We also eliminated dependency on the implementation of the automobile classes. 
The main program knows only that those classes implement the abstract methods 
in the abstract base class.

One thing to note, though, we're limited to one factory.
"""

class AbsAuto(ABC):
    """
    Here are the two abstract methods that must be implemented by
    the concrete classes
    """

    @abstractmethod
    def start(self):
        """
        start the car
        """

    @abstractmethod
    def stop(self):
        """
        stop the car
        """

class ChevyVolt(AbsAuto):
    def start(self):
        print('ChevyVolt running with shocking power!')

    def stop(self):
        print('ChevyVolt shutting down.')

class FordFusion(AbsAuto):
    def start(self):
        print('FordFusion running with shocking power!')

    def stop(self):
        print('FordFusion shutting down.')

class JeepSahara(AbsAuto):
    def start(self):
        print('JeepSahara running with shocking power!')

    def stop(self):
        print('JeepSahara shutting down.')


class NullCar(AbsAuto):

    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('start method unknown car "%s".' % self._carname)

    def stop(self):
        print('stop method unknown car "%s".' % self._carname)


class AutoFactory:
    """
    This class has the job of creating and returning an instance of the
    desired auto class. This factory encapsulate class instantiation.
    """

    autos = {}  # keeps the automobile names and classes in a dictionary where the key is the name of the car model, and the value is a reference to the class for that car.

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        """
        Builds the dictionary
        Uses the introspection function getmembers to find the classes.
        """
        # getmembers: return all the members of an object in a list of (name, value) pairs sorted by name.
        classes = getmembers(sys.modules[__name__], lambda m: isclass(m) and not isabstract(m))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, AbsAuto):
                self.autos.update([[name, _type]])

    def create_instance(self, carname):
        if carname in self.autos:
            return self.autos[carname]()  # obtengo una instancia de la clase
        else:
            return NullCar(carname)  # es mejor retornar null que otra cosa


if __name__ == '__main__':
    """
    Now it simply and instantiates the AutoFactory class and get an instance
    of each Car.
    It encapsulates object instantiation. We no longer have 
    to instantiate classes directly. Instead, we call a factory method to do 
    it for us. And this supports the dependency inversion principle. 
    Client programs are no longer dependent on the implementations of 
    the classes they use. In fact, they do not even need to know the names of 
    them. Instead, clients depend upon an abstraction.
    """
    factory = AutoFactory()

    for carname in 'ChevyVolt', 'FordFusion', 'JeepSahara', 'Tesla Roadster':
        car = factory.create_instance(carname)  # we call a factory method to do it for us.
        car.start()
        car.stop()
