from typing import List, Tuple


class Customer:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address


class Vendor:
    def __init__(self, name, number, street):
        self._name = name
        self._number = number
        self._street = street

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @property
    def street(self):
        return self._street


class VendorAdapter(Vendor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def address(self):
        return f'{self.street} {self.number}'


def client(assets: Tuple):
    for entity in assets:
        print(f'Name: {entity.name}. Address: {entity.address}')


if __name__ == '__main__':
    ASSETS = (
        Customer('Cristian', 'Gorostiaga 3818'),
        Customer('Gonzalo', 'San Nicolas 2546'),
        Customer('Juan', 'Buenos Aires 1535'),

        VendorAdapter('Pedro  Giani', 3621, 'Lamadrid'),
        VendorAdapter('Eduardo Avaria', 4080, 'Aurora'),
    )

    client(assets=ASSETS)
