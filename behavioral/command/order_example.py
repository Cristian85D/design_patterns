from abc import ABC, abstractmethod


class Order(ABC):  # Command

    def __init__(self, stock):
        self.stock = stock

    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):  # Concrete Command

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):  # Concrete Command

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self):
        self.stock.sell()


class StockTrade:  # Receiver

    def buy(self):
        print('You will buy stocks')

    def sell(self):
        print('You will sell stocks')


class Agent:  # Invoker
    def __init__(self):
        self.order_queue = []

    def place_order(self, order):
        self.order_queue.append(order)
        order.execute()


if __name__ == '__main__':
    # Client
    stock = StockTrade()
    buy_stock = BuyStockOrder(stock)
    sell_stock = SellStockOrder(stock)

    # Invoker
    agent = Agent()
    agent.place_order(buy_stock)
    agent.place_order(sell_stock)

    print(agent.order_queue)
