from typing import List

from abc import ABC, abstractmethod


class ComputerState(ABC):  # Abstract State
    """
    It does the changes states whenever possible.
    """

    @property
    def name(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def allowed(self) -> List[str]:
        """
        :return: list of the allowed states
        """

    def switch(self, new_state):
        """
        Validates if a change state is possible.
        """
        if new_state in self.allowed:
            print(f'Current: {self}, switched to new state: '
                  f'{new_state().__class__.__name__}')
            self.__class__ = new_state
        else:
            print(f'Current: {self}, switched to state: '
                  f'{new_state().__class__.__name__} not possible!')

    def __str__(self):
        return self.name


class Off(ComputerState):  # Concrete State

    @property
    def allowed(self):
        return [On]


class On(ComputerState): # Concrete State

    @property
    def allowed(self):
        return [Off, Suspend, Hibernate]


class Suspend(ComputerState): # Concrete State

    @property
    def allowed(self):
        return [On]


class Hibernate(ComputerState): # Concrete State

    @property
    def allowed(self):
        return [On]


class Computer:  # Context
    """
    It also maintains a reference to the object's current state.
    Accepts the client's request.
    """
    def __init__(self, model='HP'):
        """
        Defines the base/initial state of the computer
        :param model:
        """
        self.model = model
        self.state = Off()  # base/initial state

    def change_state(self, concrete_state):
        """
        Will change the state of the object(self.state), and the actual change
        in bahavior is implemented by the ConcreteState
        classes(On, Off, Suspend and Hibernate)
        :param concrete_state: On, Off, Suspend and Hibernate
        """
        self.state.switch(concrete_state)


def client():
    comp = Computer()
    comp.change_state(On)  # switch On
    comp.change_state(Off)  # switch Off

    comp.change_state(On)  # switch On again
    comp.change_state(Suspend)  # suspend

    comp.change_state(Hibernate)  # Try to hibernate - cannot!

    comp.change_state(On)  # switch On back
    comp.change_state(On)  # finally Off


if __name__ == '__main__':
    client()
