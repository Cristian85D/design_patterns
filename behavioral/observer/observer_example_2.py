from abc import ABC, abstractmethod


class NewsPublisher:

    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    @property
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()  # cada subscriber actualiza lo necesario

    def add_news(self, news):
        self.__latest_news = news

    @property
    def get_news(self):
        return 'Got News: ', self.__latest_news


class Subscriber(ABC):

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):

    def __init__(self, publisher):
        """
        :param publisher:
        """
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        self.__latest_news = self.publisher.get_news
        print(type(self).__name__, self.__latest_news)


class EmailSubscriber(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        self.__latest_news = self.publisher.get_news  # publisher set news
        print(type(self).__name__, self.__latest_news)


class AnyOtherSubscriber(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        self.__latest_news = self.publisher.get_news
        print(type(self).__name__, self.__latest_news)


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscriber(news_publisher)  # instancio cada subscriber

    print('Subscribers: ', news_publisher.subscribers)

    # add news and notify for all subscriber
    news_publisher.add_news('Hello World!')
    news_publisher.notify_subscribers()  # el publisher debe informar a cada subscriber

    print('Detached: ', type(news_publisher.detach()).__name__)
    print('Subscribers: ', news_publisher.subscribers)

    news_publisher.add_news('My Second News!')
    news_publisher.notify_subscribers()
