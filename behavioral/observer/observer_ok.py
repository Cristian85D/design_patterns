from abc import ABC, abstractmethod

"""
Dashboard
For a motivating example, consider a dashboard application for a technical 
support center. The dashboard will need to show key performance indicators, 
or KPIs, which may include the number of open tickets or issues, the number of 
new ones in the last hour, or the number of tickets closed in some period. 
In this example, the dashboard is the observer. The source of the KPIs is the 
publisher or subject. Keep in mind that other observers may be required later, 
perhaps one that shows historical averages of the same data, or another that 
shows forecasts for the next hour or day. 
"""


class AbsObserver(ABC):  # AbsObserver
    """
    The Concrete Observer implements the update method, and when the subject
    state changes, it loops(recorre) through all currently attached observers
    and calls their update methods.
    """

    @abstractmethod
    def update(self):
        pass


class Subject:  # AbsSubject > KPIs hereda de el
    """
    First, there is an abstract subject which contains the required methods
    Attach, Detach, and Notify.
    """
    _observers = set()  # collections of observers that them notified when the state of objects changed.

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self._observers |= {observer}  # agrega el observer al set

    def detach(self, observer):
        self._observers -= {observer}  # saca el observer del set

    def notify(self):
        for observer in self._observers:
            observer.update()  # cada observador actualiza los valores


class KPIs(Subject):  # ConcreteSubject
    """
    KPIs: key performance indicators
    The source of the KPIs is the publisher or subject.
    The concrete subject implements the required methods.
    Establece y notifica
    """

    @property
    def open_tickets(self): # GetState method, so observers can use that to get the subject state when it changes.
        return self._open_tickets

    @property
    def closed_tickets(self):  # GetState method, so observers can use that to get the subject state when it changes.
        return self._closed_tickets

    @property
    def new_tickets(self):  # GetState method, so observers can use that to get the subject state when it changes.
        return self._new_tickets

    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        """
        cada vez que hago un set de valores, actualizo el observer
        """
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets
        self.notify()  # un observador siempre notifica para actualizar los observadores


class CurrentKPIs(AbsObserver):  # ConcreteObserver
    """
    The Concrete Observer implements the update method, and when the subject
    state changes, it loops(recorre) through all currently attached observers
    and calls their update methods. When called, the observer's update methods
    can then call the subject's getState method to find out what changed.
    In response, the subject returns the state requested.
    Now following(siguiendo) the observer pattern, we'll separate the
    concerns(preocupaciones) of the subject, observer, and main program,
    and doing that falls(ajustara) in line with a single responsibility
    principle.
    """

    def __init__(self, kpis: KPIs):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        """
        When called, the observer's update methods can then call the subject's
        getState method to find out what changed. In response, the subject
        returns the state requested.
        """
        self.open_tickets = self._kpis.open_tickets  # obtiene los estados de _kpis compuesto y el observador actualiza sus valores
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print(f'Current open tickets: {self.open_tickets}')
        print(f'New tickets in last hour: {self.new_tickets}')
        print(f'Tickets closed in last hour: {self.closed_tickets}')
        print('*****\n')


class ForecastKPIs(AbsObserver):

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print(f'Forecast open tickets: {self.open_tickets}')  # Forecast open tickets: prevision de tickets abiertos
        print(f'New tickets expected in next hour: {self.new_tickets}')
        print(f'Tickets expected to be closed in next hour: {self.closed_tickets}')
        print('*****\n')


def main():
    # Report on current KPI values. KPIs: key performaance indicators
    kpis = KPIs()  # KPIs:AbsSubject > tiene el metodo attach.

    """
    Le reporto a cada AbsObserver el KPI.
    Cuando se asigna kpis a un observador, el kpis debe agregar el observador
    a la lista de observadores del AbsSubject con el metodo attach.
    Luego el kpis se usa dentro del metodo update del observador  
    """
    currentKPIs = CurrentKPIs(kpis)  # CurrentKPIs:AbsObserver > la instanciacion invoca attach
    forecastKPIs = ForecastKPIs(kpis)  # instancio otro observador

    """
    El kpi informa estadisticas(kpis.set_kpis()) open_tickets, closed_tickets, 
    new_tickets y cada vez que se establecen valores se deben notificar a 
    los observadores con el metodo notify() que tiene el kpis.
   
        def set_kpis(self, open_tickets, closed_tickets, new_tickets):
            self._open_tickets = open_tickets
            self._closed_tickets = closed_tickets
            self._new_tickets = new_tickets
            self.notify()

    El kpis hace todoo, establece valores y notifica a los observadores
    
    Cuando se le notifica a los observadores, se itera por cada observador 
    y se ejecuta el metodo update de cada observador y actualiza los 
    valores de: open_tickets, closed_tickets, new_tickets.

        def notify(self, value=None):
            for observer in self._observers:
                if value is None:
                    observer.update(None)
                else:
                    observer.update(value)

    Cuando un observador ejecuta el metodo update, como el observador 
    tiene al self._kpis cuando se instancio(CurrentKPIs(kpis)o ForecastKPIs(kpis))
    saca los valores que trae el self._kpis y lo asigna a sus propias variables
    de instancia y finalmente ejecuta el metodo display:
        def update(self, value=None):
            self.open_tickets = self._kpis.open_tickets
            self.closed_tickets = self._kpis.closed_tickets
            self.new_tickets = self._kpis.new_tickets
            self.display()
    """
    kpis.set_kpis(open_tickets=25, closed_tickets=10, new_tickets=5)
    kpis.set_kpis(open_tickets=100, closed_tickets=50, new_tickets=30)
    kpis.set_kpis(open_tickets=50, closed_tickets=10, new_tickets=20)

    print(f'\n***Detaching the currentKPIs observer.***\n\n')
    kpis.detach(currentKPIs)  # saco un observador
    kpis.set_kpis(open_tickets=150, closed_tickets=110, new_tickets=120)


if __name__ == '__main__':
    main()
