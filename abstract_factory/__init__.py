from abc import ABCMeta, abstractmethod


class AbstractProductA(metaclass=ABCMeta):
    pass


class SpecificProductAMacOS(AbstractProductA):
    pass


class SpecificProductAWin(AbstractProductA):
    pass


class AbstractProductB(metaclass=ABCMeta):
    pass


class SpecificProductBMacOS(AbstractProductB):
    pass


class SpecificProductBWin(AbstractProductB):
    pass


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class SpecificFactoryMacOS(AbstractFactory):
    def create_product_a(self):
        return SpecificProductAMacOS()

    def create_product_b(self):
        return SpecificProductBMacOS()


class SpecificFactoryWin(AbstractFactory):
    def create_product_a(self):
        return SpecificProductAWin()

    def create_product_b(self):
        return SpecificProductBWin()
