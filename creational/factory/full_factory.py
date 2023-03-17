import sys

from inspect import getmembers, isclass, isabstract
from abc import ABC, abstractmethod


"""
What if we need more factories for flexibility? 
Well, the classic factory pattern is what we need.

There will be one factory per product type.

The full factory pattern adds an abstract factory base class, and many 
factories and many factory types can be implemented, and those 
implementations can vary.
A complex factory might use other patterns to help, such as the builder 
pattern.

"""

class AbsProduct(ABC):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class ChevyVolt(AbsProduct):

    def start(self):
        print(f'{self.name} running with shocking power!')

    def stop(self):
        print(f'{self.name} shutting down.')


class FordFusion(AbsProduct):

    def start(self):
        print(f'{self.name} running with shocking power!')

    def stop(self):
        print(f'{self.name} shutting down.')


class JeepSahara(AbsProduct):

    def start(self):
        print(f'{self.name} running with shocking power!')

    def stop(self):
        print(f'{self.name} shutting down.')


class NullCar(AbsProduct):

    def start(self):
        print(f'Unknown car {self.name}')

    def stop(self):
        pass


# There will be one factory per product type

class AbsFactory(ABC):

    @abstractmethod
    def create_auto(self):
        """
        concrete factory that will be produced
        """


class ChevyFactory(AbsFactory):

    def create_auto(self):
        self.chevy = ChevyVolt()
        self.chevy.name = 'Chevy Volt'
        return self.chevy


class FordFusionFactory(AbsFactory):

    def create_auto(self):
        self.ford_fusion = FordFusion()
        self.ford_fusion.name = 'Ford Fusion'
        return self.ford_fusion


class JeepFactory(AbsFactory):

    def create_auto(self):
        self.jeep = JeepSahara()
        self.jeep.name = 'Jeep Sahara'
        return self.jeep


class NullFactory(AbsFactory):
    """
    concrete factory
    """

    def create_auto(self):
        self.nullcar =  NullCar()
        self.nullcar.name = 'Unknown'
        return self.nullcar


def load_factory(factory_name):
    """
    Las factories no estan cargadas en ningun lado previamente
    The factory loader encapsulates the logic of finding and instantiating
    the factories.
    """
    try:
        _class = eval(factory_name)
        if isclass(_class) and not isabstract(_class):
            if issubclass(_class, AbsFactory):
                return _class()
    except NameError:
        return NullFactory()


def factories_names():
    classes = getmembers(
        sys.modules[__name__],
        lambda m: isclass(m) and not isabstract(m)
    )

    # return a list with only factoriess names
    return [name for name, _type in classes if isclass(_type) and issubclass(_type, AbsFactory) and _type is not NullFactory]


if __name__ == '__main__':
    for name in factories_names():  # el cliente debe conocer el nombre de las clases.
        factory = load_factory(name)  # se obtiene la factory
        car = factory.create_auto()  # la factory crea su auto

        car.start()
        car.stop()
