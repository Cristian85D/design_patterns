from abc import ABC, abstractmethod


class AbsCar(ABC):

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


class ChevyCorsa(AbsCar):

    def start(self):
        print(f'{self.name} start')

    def stop(self):
        print(f'{self.name} stop')


class ChevyCamaro(AbsCar):

    def start(self):
        print(f'{self.name} start')

    def stop(self):
        print(f'{self.name} stop')


class ChevySpark(AbsCar):

    def start(self):
        print(f'{self.name} start')

    def stop(self):
        print(f'{self.name} stop')


class FordFiesta(AbsCar):

    def start(self):
        print(f'{self.name} start')

    def stop(self):
        print(f'{self.name} stop')


class FordK(AbsCar):

    def start(self):
        print(f'{self.name} start')

    def stop(self):
        print(f'{self.name} stop')


class FordMustang(AbsCar):

    def start(self):
        print(f'{self.name} start')

    def stop(self):
        print(f'{self.name} stop')


class AbsFactory(ABC):
    """
    Each factory makes cars for one manufacturer, but can make them in
    economy, sport, and luxury editions. Now we want to support multiple car
    manufacturers, each one having those three editions.
    """

    @abstractmethod
    def create_economy(self):
        pass

    @abstractmethod
    def create_sport(self):
        pass

    @abstractmethod
    def create_luxury(self):
        pass


"""
There are two concrete factories, one each for Ford and GM.
"""

class FordFactory(AbsFactory):

    def create_economy(self):
        self.ford_fiesta = FordFiesta()
        self.ford_fiesta.name = 'Ford Fiesta'
        return self.ford_fiesta

    def create_sport(self):
        self.ford_k = FordK()
        self.ford_k.name = 'Ford K'
        return self.ford_k

    def create_luxury(self):
        self.ford_mustang = FordMustang()
        self.ford_mustang.name = 'Ford Mustang'
        return self.ford_mustang


class GeneralMotorsFactory(AbsFactory):

    def create_economy(self):
        self.chevy_corsa = ChevyCorsa()
        self.chevy_corsa.name = 'Chevy Corsa'
        return self.chevy_corsa

    def create_sport(self):
        self.chevy_spark = ChevySpark()
        self.chevy_spark.name = 'Chevy Spark'
        return self.chevy_spark

    def create_luxury(self):
        self.chevy_camaro = ChevyCamaro()
        self.chevy_camaro.name = 'Chevy Camaro'
        return self.chevy_camaro


def client():

    for factory in FordFactory(), GeneralMotorsFactory():
        car = factory.create_economy()
        car.start()
        car.stop()
        car = factory.create_sport()
        car.start()
        car.stop()
        car = factory.create_luxury()
        car.start()
        car.stop()


if __name__ == '__main__':
    client()
