from abc import ABC


class Command(ABC):
    """
    This declare an interface to execute an operation
    """
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        pass


class ConcreteCommand(Command):
    """
    this defines a binding between the Receiver object and action
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self):
        self.recv.action()


class Receiver:
    """
    This knows how to perform the operations associated with carrying out
    the request
    """
    def action(self):
        print('Receiver action')


class Invoker:
    """
    This asks ConcreteCommand object and sets its receiver
    """
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


if __name__ == '__main__':
    recv = Receiver()
    cmd = ConcreteCommand(recv)

    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
