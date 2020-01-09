import abc


class CustomerRepository(abc.ABC):
    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_by_id(self, customer_id):
        pass

    @abc.abstractmethod
    def add(self, customer):
        pass


class EventRepository(abc.ABC):
    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_by_id(self, event_id):
        pass

    @abc.abstractmethod
    def add(self, event):
        pass


class OrderRepository(abc.ABC):
    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_by_id(self, order_id):
        pass

    @abc.abstractmethod
    def add(self, order):
        pass
