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
