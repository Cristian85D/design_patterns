
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
