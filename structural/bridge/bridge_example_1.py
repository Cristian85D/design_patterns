from abc import ABC, abstractmethod
from dateutil.relativedelta import relativedelta
from datetime import datetime


class Subscription(ABC):

    def __init__(self, subscriber, enrolled, discount):
        self._subscriber = subscriber
        self._enrolled = enrolled
        self._discount = discount()

    @property
    def subscriber(self):
        return self._subscriber

    @property
    def enrolled(self):
        return self._enrolled

    @property
    @abstractmethod
    def price_base(self):
        """
        Is set when the abstract class Subscription is implemented
        A subscription can be Annual or Monthly
        Each subscription has a price base
        """

    @property
    def price(self):
        discount = self._discount.discount
        print(f'Subscriber: {self.subscriber} '
              f'Price Base: {self.price_base} '
              f'Type discount: {self._discount.__class__.__name__} '
              f'Discount: {discount}')
        return self.price_base * (1 - discount / 100)

    @property
    @abstractmethod
    def expiration(self):
        """
        Is set when the abstract class Subscription is implemented
        A subscription can be Annual or Monthly
        Each
        """


class Annual(Subscription):
    """
    Refined Abstraction
    """

    @property
    def price_base(self):
        return 250.00

    @property
    def expiration(self):
        return self._enrolled + relativedelta(years=1)


class Monthly(Subscription):
    """
    Refined Abstraction
    """

    @property
    def price_base(self):
        return 50.00

    @property
    def expiration(self):
        return self._enrolled + relativedelta(months=1)


class Discount(ABC):
    """
    Implementor
    """

    @property
    @abstractmethod
    def discount(self):
        pass


class StudentDiscount(Discount):
    """
    concrete implementor
    """

    @property
    def discount(self):
        return 10


class CorporateDiscount(Discount):
    """
    concrete implementor
    """

    @property
    def discount(self):
        return 20


class NoDiscount(Discount):
    """
    concrete implementor
    """

    @property
    def discount(self):
        return 0


def main():
    sub1 = Monthly('Ted', datetime.today(), StudentDiscount)
    #sub2 = Annual('Alice', datetime.today(), CorporateDiscount)
    #sub3 = Annual('Bob', datetime.today(), NoDiscount)

    print(f'Subscription: {sub1.subscriber}, Cost: {sub1.price}, '
          f'Expiration: {sub1.expiration}')
    # print(f'Subscription: {sub2.subscriber}, Cost: {sub2.price}, '
    #       f'Expiration: {sub2.expiration}')
    # print(f'Subscription: {sub3.subscriber}, Cost: {sub3.price}, '
    #       f'Expiration: {sub3.expiration}')


if __name__ == "__main__":
    main()
