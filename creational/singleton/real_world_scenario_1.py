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
