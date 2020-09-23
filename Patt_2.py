from abc import ABC, abstractmethod
import random


class AbstractFactory(ABC):
    @abstractmethod
    def create_minivan(self):
        pass

    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_cabriolet(self):
        pass


class AudiFactory(AbstractFactory):
    def create_minivan(self):
        return Minivan()

    def create_sedan(self):
        return Sedan()

    def create_cabriolet(self):
        return Cabriolet()


class BMWFactory(AbstractFactory):
    def create_minivan(self):
        return Minivan()

    def create_sedan(self):
        return Sedan()

    def create_cabriolet(self):
        return Cabriolet()


class ToyotaFactory(AbstractFactory):
    def create_minivan(self):
        return Minivan()

    def create_sedan(self):
        return Sedan()

    def create_cabriolet(self):
        return Cabriolet()


class Minivan:
    def __init__(self):
        self.color = None
        self.equipment = None
        self.model = None

    def add_color(self, color):
        self.color = color

    def add_equipment(self, equipment):
        self.equipment = equipment

    def add_model(self, model):
        self.model = model

    def info(self):
        print(f"Model: {self.model}, color: {self.color}, equipment: {self.equipment}")


class Sedan:
    def __init__(self):
        self.color = None
        self.equipment = None
        self.model = None

    def add_color(self, color):
        self.color = color

    def add_equipment(self, equipment):
        self.equipment = equipment

    def add_model(self, model):
        self.model = model

    def info(self):
        print(f"Model: {self.model}, color: {self.color}, equipment: {self.equipment}")


class Cabriolet:
    def __init__(self):
        self.color = None
        self.equipment = None
        self.model = None

    def add_color(self, color):
        self.color = color

    def add_equipment(self, equipment):
        self.equipment = equipment

    def add_model(self, model):
        self.model = model

    def info(self):
        print(f"Model: {self.model}, color: {self.color}, equipment: {self.equipment}")


def create_car(factory, name):

    color = ['Красный', 'Черный', 'Белый', 'Синий', 'Желтый']
    equipment = ['Classic', 'Comfort', 'Luxe', 'Premium']

    if name == 'minivan':
        car = factory.create_minivan()

        model = ['A6', 'A7', 'A8', 'Q6', 'Q7', 'Q8']

        car.add_color(random.choice(color))
        car.add_equipment(random.choice(equipment))
        car.add_model(random.choice(model))

        return car

    elif name == 'sedan':
        car = factory.create_minivan()

        model = ['S6', 'S7', 'S8', 'Z6', 'Z7', 'Z8']

        car.add_color(random.choice(color))
        car.add_equipment(random.choice(equipment))
        car.add_model(random.choice(model))

        return car

    elif name == 'cabriolet':
        car = factory.create_minivan()

        model = ['K16', 'K27', 'K98', 'BZ6', 'BZ7', 'BZ8']

        car.add_color(random.choice(color))
        car.add_equipment(random.choice(equipment))
        car.add_model(random.choice(model))

        return car
    else:
        return "Ошибка!"


audi_minivan = create_car(AudiFactory(), 'minivan')
bmw_sedan = create_car(BMWFactory(), 'sedan')
toyota_cabriolet = create_car(ToyotaFactory(), 'cabriolet')

audi_minivan.info()
bmw_sedan.info()
toyota_cabriolet.info()
