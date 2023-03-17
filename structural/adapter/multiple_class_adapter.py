from abc import ABC, abstractmethod


class Customer:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    @property
    def customer_name(self):
        return self._name

    @property
    def customer_address(self):
        return self._address


class Vendor:
    def __init__(self, name, number, street):
        self._name = name
        self._number = number
        self._street = street

    @property
    def vendor_name(self):
        return self._name

    @property
    def vendor_number(self):
        return self._number

    @property
    def vendor_street(self):
        return self._street


class Employee:
    def __init__(self, name, number, street, city):
        self._name = name
        self._number = number
        self._street = street
        self._city = city

    @property
    def employee_name(self):
        return self._name

    @property
    def employee_number(self):
        return self._number

    @property
    def employee_street(self):
        return self._street

    @property
    def employee_city(self):
        return self._city


class AbsAdapter(ABC):

    def __init__(self, adaptee):
        self._adaptee = adaptee

    @property
    def adaptee(self):
        return self._adaptee

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def location(self):
        pass


class CustomerAdapter(AbsAdapter):

    @property
    def name(self):
        return self.adaptee.customer_name

    @property
    def location(self):
        return self.adaptee.customer_address


class VendorAdapter(AbsAdapter):
    @property
    def name(self):
        return self.adaptee.vendor_name

    @property
    def location(self):
        return f'{self.adaptee.vendor_number} {self.adaptee.vendor_street}'


class EmployeeAdapter(AbsAdapter):

    @property
    def name(self):
        return self.adaptee.employee_name

    @property
    def location(self):
        return f'{self.adaptee.employee_street} ' \
               f'{self.adaptee.employee_number} ' \
               f'{self.adaptee.employee_city}'


if __name__ == '__main__':
    ENTITIES = (
        CustomerAdapter(Customer('Cristian Gomez', 'Francia 5251')),
        CustomerAdapter(Customer('Juan Cristaldo', 'Avellaneda 1580')),

        EmployeeAdapter(Employee('Marcos', 1580, 'San Juan', 'Rosario')),
        VendorAdapter(Vendor('Nicolas', 7585, 'Juan B Justo 3598'))
    )

    for entity in ENTITIES:
        print(f'Name: {entity.name}. Location: {entity.location}')
