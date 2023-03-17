"""
Consider a way to create an object representing some model of a car.

Here I support three car models, Chevy Volt, a Ford Fusion, and a Jeep Sahara.
There's a null car too.

ChevyVolt class looks like this. It implements a start and stop method,
both of which just print messages for testing.
The other two car classes look very much the same.

Problem with this approach:
Each time we add a car, we must add one instance of it in the if-else code
from getcar method
"""

class ChevyVolt:
    """
    ChevyVolt class looks like this. It implements a start and stop method, both of which just print messages for testing.
    """
    def start(self):
        print('Chevrolet Volt running with shocking power!')

    def stop(self):
        print('Chevrolet Volt shutting down.')


class FordFusion:
    def start(self):
        print('Cool Ford Fusion running smoothly.')

    def stop(self):
        print('Ford Fusion shutting down.')


class JeepSahara:
    def start(self):
        print('Jeep Saraha running ruggedly.')

    def stop(self):
        print('Jeep Saraha shutting down.')


class NullCar:
    """
     This is actually an example of the null pattern, which basically says
     return a dummy instance that still implements all the required methods.
     This then means that I don't have to test for null objects at runtime.
    """
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('Unknown car "%s".' % self._carname)

    def stop(self):
        pass


def getcar(carname):
    """
    :param carname: Takes the name of the desired car as a parameter.
    """

    # Take note of that long if elif else statement. When you see something
    # like that in code or are tempted to write it, it can be a sign that
    # there might be a better way. The factory pattern offers a solution for just this issue.
    # Thinking about it though, if we wanted to add a different car model,
    # we'd have to open up this code, modify the getcar
    # function. That would break the open/closed principle.
    # Open‑closed principle: a class should be open for extension, usually by
    # inheritance, but closed for modification.
    # Imagine you started to use a class I designed, only to find out later
    # that I had changed it. You'd be frustrated and rightly so.
    if carname == 'Chevy':
        return ChevyVolt()
    elif carname == 'Ford':
        return FordFusion()
    elif carname == 'Jeep':
        return JeepSahara()
    else:
        return NullCar(carname)


def main():
    for carname in 'Chevy', 'Ford', 'Jeep', 'Tesla':
        car = getcar(carname)
        car.start()
        car.stop()

if __name__ == '__main__':
    main()
